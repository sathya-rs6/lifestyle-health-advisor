import gradio as gr
import json
from datetime import datetime
from database import HealthDatabase

# Initialize database
db = HealthDatabase()

def suggest_health_advanced(age, physical_activity_level, stress_level, gender, heart_rate, blood_pressure, sleep_disorder, bmi_category, daily_steps, user_name, save_data):
    suggestions = []
    risk_factors = []
    positive_factors = []

    try:
        heart_rate_val = float(heart_rate) if heart_rate else None
    except Exception:
        heart_rate_val = None
    try:
        bp_val = float(blood_pressure) if blood_pressure else None
    except Exception:
        bp_val = None
    try:
        steps_val = float(daily_steps) if daily_steps else None
    except Exception:
        steps_val = None

    # Age-based recommendations
    if age is not None:
        if age <= 12:
            suggestions.append("👶 **Child Health Focus**: Ensure 9-12 hours of sleep, limit screen time to 2 hours/day, and encourage 60+ minutes of physical activity.")
            if physical_activity_level and physical_activity_level <= 2:
                suggestions.append("🏃 **Activity Boost**: Encourage outdoor play, sports, or active games. Consider family activities like hiking or cycling.")
        elif age <= 18:
            suggestions.append("🧑‍🎓 **Teen Health**: Focus on consistent sleep schedule (8-10 hours), balanced nutrition, and stress management during academic periods.")
        elif age <= 30:
            suggestions.append("💪 **Young Adult**: Build healthy habits now! Focus on regular exercise, stress management, and preventive healthcare.")
        elif age <= 50:
            suggestions.append("👨‍💼 **Mid-Life Health**: Prioritize cardiovascular health, maintain muscle mass through strength training, and manage work-life balance.")
        else:
            suggestions.append("🧓 **Senior Health**: Focus on bone health, cognitive stimulation, social connections, and regular health screenings.")

    # Physical Activity Analysis
    if physical_activity_level is not None:
        if physical_activity_level <= 2:
            risk_factors.append("Low physical activity")
            suggestions.append("🚶 **Activity Recommendation**: Start with 10-minute walks, gradually increase to 150 minutes/week of moderate activity.")
            suggestions.append("💡 **Quick Tips**: Take stairs, park farther away, do desk exercises, or try home workout videos.")
        elif physical_activity_level <= 5:
            suggestions.append("👍 **Good Start**: You're moderately active! Consider adding strength training 2x/week and increasing intensity gradually.")
        elif physical_activity_level <= 8:
            suggestions.append("🏆 **Excellent Activity Level**: Great job! Maintain your routine and consider adding variety with different activities.")
        else:
            suggestions.append("🔥 **High Activity**: Outstanding! Ensure proper recovery, nutrition, and listen to your body to prevent overtraining.")

    # Stress Management
    if stress_level is not None:
        if stress_level >= 8:
            risk_factors.append("High stress level")
            suggestions.append("😰 **High Stress Alert**: Consider professional help, practice daily meditation, deep breathing, or progressive muscle relaxation.")
            suggestions.append("🌱 **Stress Relief**: Try yoga, nature walks, journaling, or hobbies. Limit caffeine and ensure adequate sleep.")
        elif stress_level >= 6:
            suggestions.append("⚠️ **Moderate Stress**: Practice stress management techniques like mindfulness, regular breaks, and time management.")
        elif stress_level <= 3:
            positive_factors.append("Low stress level")
            suggestions.append("😊 **Great Stress Management**: Keep up your stress management practices!")

    # Sleep Disorder Management
    if isinstance(sleep_disorder, str) and sleep_disorder.strip():
        sleep_disorder_lower = sleep_disorder.lower()
        if "insomnia" in sleep_disorder_lower:
            risk_factors.append("Insomnia")
            suggestions.append("😴 **Insomnia Management**: Maintain consistent sleep schedule, limit caffeine after 2 PM, create dark/cool bedroom environment.")
            suggestions.append("🍯 **Sleep Hygiene**: Avoid screens 1 hour before bed, try chamomile tea, warm bath, or light reading.")
        elif "apnea" in sleep_disorder_lower:
            risk_factors.append("Sleep apnea")
            suggestions.append("🫁 **Sleep Apnea**: Consult a sleep specialist. Consider weight management, avoid alcohol before bed, and sleep on your side.")
        elif "none" not in sleep_disorder_lower:
            suggestions.append("🛌 **Sleep Health**: Maintain regular sleep schedule, 7-9 hours nightly, and create a relaxing bedtime routine.")

    # Cardiovascular Health
    if heart_rate_val is not None:
        if heart_rate_val > 100:
            risk_factors.append("Elevated heart rate")
            suggestions.append("💓 **Heart Rate Alert**: Resting HR >100 may indicate stress, dehydration, or medical condition. Monitor and consult healthcare provider.")
        elif heart_rate_val < 60:
            suggestions.append("💪 **Athletic Heart**: Low resting HR can indicate good fitness, but consult doctor if experiencing symptoms.")
        else:
            positive_factors.append("Normal heart rate")

    if bp_val is not None:
        if bp_val > 140:
            risk_factors.append("High blood pressure")
            suggestions.append("🩸 **High Blood Pressure**: Reduce sodium intake, increase potassium-rich foods, regular exercise, and consult healthcare provider.")
        elif bp_val > 120:
            risk_factors.append("Elevated blood pressure")
            suggestions.append("⚠️ **Pre-Hypertension**: Focus on DASH diet, weight management, stress reduction, and regular monitoring.")
        else:
            positive_factors.append("Normal blood pressure")

    # BMI and Weight Management
    if bmi_category and bmi_category != "Normal":
        if "Underweight" in bmi_category:
            suggestions.append("📈 **Weight Gain**: Focus on nutrient-dense foods, strength training, and consult nutritionist for healthy weight gain.")
        elif "Overweight" in bmi_category or "Obese" in bmi_category:
            risk_factors.append("Weight management needed")
            suggestions.append("⚖️ **Weight Management**: Create calorie deficit through diet and exercise, focus on whole foods, and consider professional guidance.")

    # Daily Steps Analysis
    if steps_val is not None:
        if steps_val < 5000:
            risk_factors.append("Low daily activity")
            suggestions.append("👟 **Step Goal**: Aim for 7,000-10,000 steps daily. Start with small increases, use step tracker, take walking breaks.")
        elif steps_val < 8000:
            suggestions.append("🚶 **Good Progress**: You're getting close to optimal step count! Try adding 1,000 more steps daily.")
        else:
            positive_factors.append("Excellent daily activity")

    # Gender-specific recommendations
    if gender:
        if gender.lower() == "female":
            suggestions.append("👩 **Women's Health**: Consider iron-rich foods, calcium for bone health, and regular health screenings.")
        else:
            suggestions.append("👨 **Men's Health**: Focus on heart health, prostate awareness, and regular health checkups.")

    # Comprehensive Health Summary
    if risk_factors:
        suggestions.append(f"\n🚨 **Risk Factors Identified**: {', '.join(risk_factors)}")
        suggestions.append("💡 **Priority Actions**: Address these areas first for optimal health improvement.")
    
    if positive_factors:
        suggestions.append(f"\n✅ **Health Strengths**: {', '.join(positive_factors)}")
        suggestions.append("🌟 **Keep It Up**: Continue these healthy practices!")

    # General wellness tips
    suggestions.append("\n🌿 **General Wellness**: Stay hydrated (8 glasses water/day), eat colorful fruits/vegetables, and maintain social connections.")

    if not suggestions:
        suggestions.append("📝 **Complete Your Profile**: Fill in more details to receive personalized health recommendations!")

    suggestions_text = "\n".join(suggestions)

    # Save data if requested
    save_status = ""
    if save_data and user_name and user_name.strip():
        try:
            # Create or get user
            user_id = db.create_user(
                name=user_name.strip(),
                age=age,
                gender=gender
            )
            
            # Save health record
            health_data = {
                'physical_activity_level': physical_activity_level,
                'stress_level': stress_level,
                'heart_rate': heart_rate_val,
                'blood_pressure': bp_val,
                'sleep_disorder': sleep_disorder,
                'bmi_category': bmi_category,
                'daily_steps': steps_val,
                'suggestions': suggestions_text,
                'risk_factors': risk_factors,
                'positive_factors': positive_factors
            }
            
            record_id = db.save_health_record(user_id, health_data)
            
            # Save analytics
            if physical_activity_level is not None:
                db.save_health_analytics(user_id, 'physical_activity', physical_activity_level)
            if stress_level is not None:
                db.save_health_analytics(user_id, 'stress_level', stress_level)
            if heart_rate_val is not None:
                db.save_health_analytics(user_id, 'heart_rate', heart_rate_val)
            if bp_val is not None:
                db.save_health_analytics(user_id, 'blood_pressure', bp_val)
            if steps_val is not None:
                db.save_health_analytics(user_id, 'daily_steps', steps_val)
            
            save_status = f"\n\n💾 **Data Saved Successfully!**\nUser ID: {user_id} | Record ID: {record_id}\nYour health data has been stored for future reference and tracking."
            
        except Exception as e:
            save_status = f"\n\n❌ **Save Error**: {str(e)}"

    return suggestions_text + save_status

def get_user_dashboard(user_id):
    """Get user dashboard data"""
    if not user_id or user_id <= 0:
        return "Please enter a valid User ID"
    
    try:
        user = db.get_user(user_id)
        if not user:
            return f"User with ID {user_id} not found"
        
        health_history = db.get_user_health_history(user_id, limit=10)
        analytics = db.get_health_analytics(user_id)
        
        dashboard = f"""
# 📊 Health Dashboard for {user['name']}

## 👤 User Information
- **Name**: {user['name']}
- **Age**: {user['age'] or 'Not specified'}
- **Gender**: {user['gender'] or 'Not specified'}
- **Member Since**: {user['created_at']}

## 📈 Recent Health Records ({len(health_history)} records)
"""
        
        if health_history:
            for i, record in enumerate(health_history[:5], 1):
                dashboard += f"""
### Record #{i} - {record['created_at'][:10]}
- **Activity Level**: {record['physical_activity_level'] or 'N/A'}/10
- **Stress Level**: {record['stress_level'] or 'N/A'}/10
- **Heart Rate**: {record['heart_rate'] or 'N/A'} bpm
- **Blood Pressure**: {record['blood_pressure'] or 'N/A'} mmHg
- **Daily Steps**: {record['daily_steps'] or 'N/A'}
- **BMI Category**: {record['bmi_category'] or 'N/A'}
- **Sleep Disorder**: {record['sleep_disorder'] or 'None'}
"""
        else:
            dashboard += "No health records found."
        
        # Analytics summary
        if analytics:
            dashboard += "\n## 📊 Health Trends\n"
            metrics = {}
            for analytic in analytics:
                metric = analytic['metric_name']
                if metric not in metrics:
                    metrics[metric] = []
                metrics[metric].append(analytic['metric_value'])
            
            for metric, values in metrics.items():
                if values:
                    avg_value = sum(values) / len(values)
                    dashboard += f"- **{metric.replace('_', ' ').title()}**: Average {avg_value:.1f} (from {len(values)} records)\n"
        
        return dashboard
        
    except Exception as e:
        return f"Error loading dashboard: {str(e)}"

# Custom CSS for better styling
css = """
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 1400px !important;
    margin: 0 auto !important;
}
.main-header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}
.health-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 4px solid #667eea;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.suggestion-output {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    border-radius: 15px;
    padding: 1.5rem;
    font-size: 14px;
    line-height: 1.6;
}
.dashboard-output {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    border-radius: 15px;
    padding: 1.5rem;
    font-size: 14px;
    line-height: 1.6;
}
.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 600;
    color: white;
    transition: all 0.3s ease;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
"""

with gr.Blocks(title="🏥 Advanced Lifestyle Health Advisor", css=css, theme=gr.themes.Soft()) as demo:
    # Header Section
    with gr.Row():
        gr.HTML("""
        <div class="main-header">
            <h1>🏥 Advanced Lifestyle Health Advisor</h1>
            <p>Get personalized health recommendations with data storage and analytics</p>
            <p style="font-size: 14px; opacity: 0.9;">Powered by AI • Data Storage Enabled • Health Tracking</p>
        </div>
        """)
    
    # Main Interface with Tabs
    with gr.Tabs():
        # Health Assessment Tab
        with gr.Tab("🔍 Health Assessment"):
            with gr.Row():
                with gr.Column(scale=2):
                    gr.Markdown("### 📊 Personal Information")
                    with gr.Row():
                        user_name = gr.Textbox(
                            label="👤 Your Name", 
                            placeholder="Enter your name to save data",
                            info="Required for data storage"
                        )
                        age = gr.Number(
                            label="👤 Age", 
                            value=30, 
                            minimum=1, 
                            maximum=120,
                            info="Enter your current age"
                        )
                        gender = gr.Radio(
                            ["Male", "Female", "Other"], 
                            label="⚥ Gender", 
                            value="Male",
                            info="Select your gender"
                        )
                    
                    gr.Markdown("### 🏃‍♂️ Activity & Lifestyle")
                    with gr.Row():
                        physical_activity_level = gr.Slider(
                            minimum=0, 
                            maximum=10, 
                            value=5, 
                            step=0.5,
                            label="💪 Physical Activity Level (0-10)",
                            info="0 = Sedentary, 10 = Very Active"
                        )
                        stress_level = gr.Slider(
                            minimum=0, 
                            maximum=10, 
                            value=4, 
                            step=0.5,
                            label="😰 Stress Level (0-10)",
                            info="0 = Very Relaxed, 10 = Extremely Stressed"
                        )
                    
                    with gr.Row():
                        daily_steps = gr.Number(
                            label="👟 Daily Steps", 
                            value=8000,
                            info="Average steps per day"
                        )
                        bmi_category = gr.Dropdown(
                            ["Underweight", "Normal", "Overweight", "Obese"],
                            label="⚖️ BMI Category",
                            value="Normal",
                            info="Select your BMI category"
                        )
                    
                    gr.Markdown("### 🫀 Health Metrics")
                    with gr.Row():
                        heart_rate = gr.Number(
                            label="💓 Heart Rate (bpm)", 
                            value=75,
                            info="Resting heart rate"
                        )
                        blood_pressure = gr.Number(
                            label="🩸 Blood Pressure (systolic)", 
                            value=120,
                            info="Systolic blood pressure"
                        )
                    
                    sleep_disorder = gr.Dropdown(
                        ["None", "Insomnia", "Sleep Apnea", "Restless Leg Syndrome", "Other"],
                        label="😴 Sleep Disorder",
                        value="None",
                        info="Select any sleep issues you experience"
                    )
                    
                    save_data = gr.Checkbox(
                        label="💾 Save my data for tracking",
                        value=True,
                        info="Check to save your health data for future reference"
                    )
                
                # Output Section
                with gr.Column(scale=1):
                    gr.Markdown("### 💡 Health Recommendations")
                    output = gr.Textbox(
                        label="", 
                        lines=20,
                        max_lines=25,
                        show_copy_button=True,
                        elem_classes=["suggestion-output"]
                    )
            
            # Action Button
            with gr.Row():
                btn = gr.Button(
                    "🔍 Get Personalized Health Suggestions", 
                    variant="primary",
                    size="lg",
                    elem_classes=["btn-primary"]
                )
        
        # Dashboard Tab
        with gr.Tab("📊 Health Dashboard"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### 👤 View Your Health History")
                    user_id_input = gr.Number(
                        label="User ID",
                        value=1,
                        info="Enter your User ID to view dashboard"
                    )
                    dashboard_btn = gr.Button(
                        "📈 Load Dashboard",
                        variant="secondary"
                    )
                
                with gr.Column(scale=2):
                    gr.Markdown("### 📊 Your Health Dashboard")
                    dashboard_output = gr.Textbox(
                        label="",
                        lines=25,
                        max_lines=30,
                        show_copy_button=True,
                        elem_classes=["dashboard-output"]
                    )
        
        # Data Management Tab
        with gr.Tab("💾 Data Management"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### 📋 All Users")
                    users_btn = gr.Button("👥 View All Users", variant="secondary")
                    users_output = gr.Textbox(
                        label="Users List",
                        lines=10,
                        show_copy_button=True
                    )
                
                with gr.Column():
                    gr.Markdown("### 📤 Export Data")
                    export_user_id = gr.Number(
                        label="User ID to Export",
                        value=1
                    )
                    export_btn = gr.Button("📥 Export User Data", variant="secondary")
                    export_output = gr.Textbox(
                        label="Export Data (JSON)",
                        lines=15,
                        show_copy_button=True
                    )
    
    # Footer
    gr.Markdown("""
    ---
    <div style="text-align: center; color: #666; font-size: 12px;">
    <p>⚠️ <strong>Disclaimer:</strong> This tool provides general health suggestions and should not replace professional medical advice. Always consult healthcare providers for medical concerns.</p>
    <p>🔒 Your data is stored locally in SQLite database. Keep your User ID safe for accessing your health history.</p>
    </div>
    """)

    # Event Handlers
    btn.click(
        fn=suggest_health_advanced,
        inputs=[age, physical_activity_level, stress_level, gender, heart_rate, blood_pressure, sleep_disorder, bmi_category, daily_steps, user_name, save_data],
        outputs=[output],
    )
    
    dashboard_btn.click(
        fn=get_user_dashboard,
        inputs=[user_id_input],
        outputs=[dashboard_output]
    )
    
    def get_all_users():
        users = db.get_all_users()
        if not users:
            return "No users found in database."
        
        users_text = "## 👥 All Users in Database\n\n"
        for user in users:
            users_text += f"**ID {user['id']}**: {user['name']} ({user['age']} years, {user['gender']}) - Joined: {user['created_at'][:10]}\n"
        
        return users_text
    
    users_btn.click(
        fn=get_all_users,
        outputs=[users_output]
    )
    
    def export_user_data(user_id):
        if not user_id or user_id <= 0:
            return "Please enter a valid User ID"
        
        try:
            data = db.export_user_data(user_id)
            return json.dumps(data, indent=2, default=str)
        except Exception as e:
            return f"Error exporting data: {str(e)}"
    
    export_btn.click(
        fn=export_user_data,
        inputs=[export_user_id],
        outputs=[export_output]
    )

if __name__ == "__main__":
    demo.launch()
