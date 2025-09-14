import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
import os

class HealthDatabase:
    def __init__(self, db_path: str = "health_data.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                age INTEGER,
                gender TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Health records table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS health_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                physical_activity_level REAL,
                stress_level REAL,
                heart_rate REAL,
                blood_pressure REAL,
                sleep_disorder TEXT,
                bmi_category TEXT,
                daily_steps INTEGER,
                suggestions TEXT,
                risk_factors TEXT,
                positive_factors TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Health analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS health_analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                metric_name TEXT,
                metric_value REAL,
                date_recorded DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user(self, name: str, email: str = None, age: int = None, gender: str = None) -> int:
        """Create a new user and return user ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO users (name, email, age, gender)
            VALUES (?, ?, ?, ?)
        ''', (name, email, age, gender))
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return user_id
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user information by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'age': user[3],
                'gender': user[4],
                'created_at': user[5],
                'updated_at': user[6]
            }
        return None
    
    def save_health_record(self, user_id: int, health_data: Dict) -> int:
        """Save a health record for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO health_records (
                user_id, physical_activity_level, stress_level, heart_rate,
                blood_pressure, sleep_disorder, bmi_category, daily_steps,
                suggestions, risk_factors, positive_factors
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            health_data.get('physical_activity_level'),
            health_data.get('stress_level'),
            health_data.get('heart_rate'),
            health_data.get('blood_pressure'),
            health_data.get('sleep_disorder'),
            health_data.get('bmi_category'),
            health_data.get('daily_steps'),
            health_data.get('suggestions'),
            json.dumps(health_data.get('risk_factors', [])),
            json.dumps(health_data.get('positive_factors', []))
        ))
        
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return record_id
    
    def get_user_health_history(self, user_id: int, limit: int = 50) -> List[Dict]:
        """Get health history for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM health_records 
            WHERE user_id = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (user_id, limit))
        
        records = cursor.fetchall()
        conn.close()
        
        health_history = []
        for record in records:
            health_history.append({
                'id': record[0],
                'user_id': record[1],
                'physical_activity_level': record[2],
                'stress_level': record[3],
                'heart_rate': record[4],
                'blood_pressure': record[5],
                'sleep_disorder': record[6],
                'bmi_category': record[7],
                'daily_steps': record[8],
                'suggestions': record[9],
                'risk_factors': json.loads(record[10]) if record[10] else [],
                'positive_factors': json.loads(record[11]) if record[11] else [],
                'created_at': record[12]
            })
        
        return health_history
    
    def get_health_analytics(self, user_id: int, metric_name: str = None) -> List[Dict]:
        """Get health analytics for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if metric_name:
            cursor.execute('''
                SELECT * FROM health_analytics 
                WHERE user_id = ? AND metric_name = ?
                ORDER BY date_recorded DESC
            ''', (user_id, metric_name))
        else:
            cursor.execute('''
                SELECT * FROM health_analytics 
                WHERE user_id = ?
                ORDER BY date_recorded DESC
            ''', (user_id,))
        
        analytics = cursor.fetchall()
        conn.close()
        
        return [{
            'id': record[0],
            'user_id': record[1],
            'metric_name': record[2],
            'metric_value': record[3],
            'date_recorded': record[4],
            'created_at': record[5]
        } for record in analytics]
    
    def save_health_analytics(self, user_id: int, metric_name: str, metric_value: float, date_recorded: str = None):
        """Save health analytics data"""
        if not date_recorded:
            date_recorded = datetime.now().strftime('%Y-%m-%d')
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO health_analytics (user_id, metric_name, metric_value, date_recorded)
            VALUES (?, ?, ?, ?)
        ''', (user_id, metric_name, metric_value, date_recorded))
        
        conn.commit()
        conn.close()
    
    def get_all_users(self) -> List[Dict]:
        """Get all users"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
        users = cursor.fetchall()
        conn.close()
        
        return [{
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'age': user[3],
            'gender': user[4],
            'created_at': user[5],
            'updated_at': user[6]
        } for user in users]
    
    def export_user_data(self, user_id: int) -> Dict:
        """Export all user data for backup/analysis"""
        user = self.get_user(user_id)
        health_history = self.get_user_health_history(user_id, limit=1000)
        analytics = self.get_health_analytics(user_id)
        
        return {
            'user_info': user,
            'health_history': health_history,
            'analytics': analytics,
            'export_date': datetime.now().isoformat()
        }
