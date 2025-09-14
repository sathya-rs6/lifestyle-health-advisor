#!/usr/bin/env python3
"""
Test script to verify the trained model works correctly
"""

import sys
import os
sys.path.append('.')

from backend.inference import ModelBundle

def test_model():
    """Test the trained model with sample data"""
    
    print("🧪 Testing the trained model...")
    
    try:
        # Load the model
        model = ModelBundle()
        print("✅ Model loaded successfully!")
        
        # Test data - sample from the dataset
        test_data = {
            'age': 35,
            'gender': 'Male',
            'occupation': 'Engineer',
            'sleep_duration': 7.5,
            'quality_of_sleep': 8,
            'physical_activity_level': 60,
            'stress_level': 5,
            'bmi_category': 'Normal',
            'heart_rate': 70,
            'daily_steps': 8000,
            'systolic': 120,
            'diastolic': 80
        }
        
        print(f"\n📊 Test Data:")
        for key, value in test_data.items():
            print(f"   {key}: {value}")
        
        # Make prediction
        result = model.predict(test_data)
        
        print(f"\n🎯 Prediction Result:")
        print(f"   Sleep Disorder: {result['prediction']}")
        print(f"   Confidence: {result['confidence']:.3f}")
        
        # Test with different data
        test_data_2 = {
            'age': 45,
            'gender': 'Female',
            'occupation': 'Nurse',
            'sleep_duration': 6.0,
            'quality_of_sleep': 5,
            'physical_activity_level': 90,
            'stress_level': 8,
            'bmi_category': 'Overweight',
            'heart_rate': 85,
            'daily_steps': 10000,
            'systolic': 140,
            'diastolic': 90
        }
        
        print(f"\n📊 Test Data 2:")
        for key, value in test_data_2.items():
            print(f"   {key}: {value}")
        
        result_2 = model.predict(test_data_2)
        
        print(f"\n🎯 Prediction Result 2:")
        print(f"   Sleep Disorder: {result_2['prediction']}")
        print(f"   Confidence: {result_2['confidence']:.3f}")
        
        print(f"\n🎉 Model is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False

if __name__ == "__main__":
    success = test_model()
    if success:
        print("\n✅ Your model is ready for predictions!")
    else:
        print("\n❌ Model testing failed. Please check the error above.")
