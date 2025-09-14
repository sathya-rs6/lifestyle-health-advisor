import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_analyze_data():
    """Load and perform comprehensive analysis of the sleep health dataset"""
    
    # Load the dataset
    df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
    
    print("="*80)
    print("SLEEP HEALTH AND LIFESTYLE DATASET ANALYSIS")
    print("="*80)
    
    # Basic dataset information
    print(f"\n📊 DATASET OVERVIEW:")
    print(f"   • Total Records: {len(df)}")
    print(f"   • Total Features: {len(df.columns)}")
    print(f"   • Dataset Shape: {df.shape}")
    
    # Column information
    print(f"\n📋 COLUMNS:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i:2d}. {col}")
    
    # Data types
    print(f"\n🔍 DATA TYPES:")
    print(df.dtypes)
    
    # Missing values
    print(f"\n❌ MISSING VALUES:")
    missing_values = df.isnull().sum()
    if missing_values.sum() == 0:
        print("   ✅ No missing values found!")
    else:
        print(missing_values[missing_values > 0])
    
    # Basic statistics for numerical columns
    print(f"\n📈 NUMERICAL STATISTICS:")
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numerical_cols].describe().round(2))
    
    return df

def analyze_categorical_features(df):
    """Analyze categorical features in the dataset"""
    
    print(f"\n🏷️ CATEGORICAL FEATURES ANALYSIS:")
    
    categorical_cols = ['Gender', 'Occupation', 'BMI Category', 'Sleep Disorder']
    
    for col in categorical_cols:
        if col in df.columns:
            print(f"\n   📊 {col.upper()}:")
            value_counts = df[col].value_counts()
            percentages = df[col].value_counts(normalize=True) * 100
            
            for value, count in value_counts.items():
                percentage = percentages[value]
                print(f"      • {value}: {count} ({percentage:.1f}%)")

def analyze_sleep_patterns(df):
    """Analyze sleep-related patterns"""
    
    print(f"\n😴 SLEEP PATTERNS ANALYSIS:")
    
    # Sleep Duration Analysis
    print(f"\n   ⏰ SLEEP DURATION:")
    sleep_stats = df['Sleep Duration'].describe()
    print(f"      • Average: {sleep_stats['mean']:.2f} hours")
    print(f"      • Range: {sleep_stats['min']:.1f} - {sleep_stats['max']:.1f} hours")
    print(f"      • Standard Deviation: {sleep_stats['std']:.2f} hours")
    
    # Quality of Sleep Analysis
    print(f"\n   🌟 SLEEP QUALITY:")
    quality_stats = df['Quality of Sleep'].describe()
    print(f"      • Average: {quality_stats['mean']:.2f}/10")
    print(f"      • Range: {quality_stats['min']:.0f} - {quality_stats['max']:.0f}/10")
    
    # Sleep Disorders Distribution
    print(f"\n   🚨 SLEEP DISORDERS:")
    disorder_counts = df['Sleep Disorder'].value_counts()
    total_with_disorders = len(df[df['Sleep Disorder'] != 'None'])
    print(f"      • People with sleep disorders: {total_with_disorders} ({total_with_disorders/len(df)*100:.1f}%)")
    for disorder, count in disorder_counts.items():
        print(f"      • {disorder}: {count} ({count/len(df)*100:.1f}%)")

def analyze_lifestyle_factors(df):
    """Analyze lifestyle and health factors"""
    
    print(f"\n🏃 LIFESTYLE FACTORS ANALYSIS:")
    
    # Physical Activity
    print(f"\n   💪 PHYSICAL ACTIVITY:")
    activity_stats = df['Physical Activity Level'].describe()
    print(f"      • Average: {activity_stats['mean']:.1f} minutes/day")
    print(f"      • Range: {activity_stats['min']:.0f} - {activity_stats['max']:.0f} minutes/day")
    
    # Stress Levels
    print(f"\n   😰 STRESS LEVELS:")
    stress_stats = df['Stress Level'].describe()
    print(f"      • Average: {stress_stats['mean']:.1f}/10")
    print(f"      • Range: {stress_stats['min']:.0f} - {stress_stats['max']:.0f}/10")
    
    # Daily Steps
    print(f"\n   👟 DAILY STEPS:")
    steps_stats = df['Daily Steps'].describe()
    print(f"      • Average: {steps_stats['mean']:.0f} steps")
    print(f"      • Range: {steps_stats['min']:.0f} - {steps_stats['max']:.0f} steps")
    
    # BMI Categories
    print(f"\n   ⚖️ BMI DISTRIBUTION:")
    bmi_counts = df['BMI Category'].value_counts()
    for category, count in bmi_counts.items():
        print(f"      • {category}: {count} ({count/len(df)*100:.1f}%)")

def analyze_correlations(df):
    """Analyze correlations between variables"""
    
    print(f"\n🔗 CORRELATION ANALYSIS:")
    
    # Select numerical columns for correlation
    numerical_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 
                     'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']
    
    correlation_matrix = df[numerical_cols].corr()
    
    print(f"\n   📊 TOP CORRELATIONS:")
    # Get upper triangle of correlation matrix
    upper_tri = correlation_matrix.where(
        np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
    )
    
    # Find correlations > 0.3 or < -0.3
    strong_correlations = []
    for i in range(len(upper_tri.columns)):
        for j in range(i):
            corr_value = upper_tri.iloc[j, i]
            if abs(corr_value) > 0.3:
                strong_correlations.append((upper_tri.columns[j], upper_tri.columns[i], corr_value))
    
    # Sort by absolute correlation value
    strong_correlations.sort(key=lambda x: abs(x[2]), reverse=True)
    
    for var1, var2, corr in strong_correlations:
        print(f"      • {var1} ↔ {var2}: {corr:.3f}")

def analyze_by_groups(df):
    """Analyze patterns by different groups"""
    
    print(f"\n👥 GROUP-BASED ANALYSIS:")
    
    # By Gender
    print(f"\n   👨👩 BY GENDER:")
    gender_analysis = df.groupby('Gender').agg({
        'Sleep Duration': 'mean',
        'Quality of Sleep': 'mean',
        'Physical Activity Level': 'mean',
        'Stress Level': 'mean',
        'Daily Steps': 'mean'
    }).round(2)
    print(gender_analysis)
    
    # By BMI Category
    print(f"\n   ⚖️ BY BMI CATEGORY:")
    bmi_analysis = df.groupby('BMI Category').agg({
        'Sleep Duration': 'mean',
        'Quality of Sleep': 'mean',
        'Physical Activity Level': 'mean',
        'Stress Level': 'mean',
        'Daily Steps': 'mean'
    }).round(2)
    print(bmi_analysis)
    
    # By Sleep Disorder
    print(f"\n   🚨 BY SLEEP DISORDER:")
    disorder_analysis = df.groupby('Sleep Disorder').agg({
        'Sleep Duration': 'mean',
        'Quality of Sleep': 'mean',
        'Physical Activity Level': 'mean',
        'Stress Level': 'mean',
        'Daily Steps': 'mean'
    }).round(2)
    print(disorder_analysis)

def create_visualizations(df):
    """Create visualizations for the dataset"""
    
    print(f"\n📊 CREATING VISUALIZATIONS...")
    
    # Set up the plotting area
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Sleep Duration Distribution
    plt.subplot(3, 4, 1)
    plt.hist(df['Sleep Duration'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Sleep Duration Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Hours')
    plt.ylabel('Frequency')
    
    # 2. Quality of Sleep Distribution
    plt.subplot(3, 4, 2)
    plt.hist(df['Quality of Sleep'], bins=10, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('Sleep Quality Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Quality Score (1-10)')
    plt.ylabel('Frequency')
    
    # 3. Sleep Disorders Pie Chart
    plt.subplot(3, 4, 3)
    disorder_counts = df['Sleep Disorder'].value_counts()
    colors = ['lightcoral', 'lightblue', 'lightgreen', 'gold']
    plt.pie(disorder_counts.values, labels=disorder_counts.index, autopct='%1.1f%%', 
            colors=colors[:len(disorder_counts)])
    plt.title('Sleep Disorders Distribution', fontsize=12, fontweight='bold')
    
    # 4. BMI Categories
    plt.subplot(3, 4, 4)
    bmi_counts = df['BMI Category'].value_counts()
    plt.bar(bmi_counts.index, bmi_counts.values, color='orange', alpha=0.7)
    plt.title('BMI Categories Distribution', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    
    # 5. Physical Activity vs Sleep Duration
    plt.subplot(3, 4, 5)
    plt.scatter(df['Physical Activity Level'], df['Sleep Duration'], alpha=0.6, color='purple')
    plt.title('Physical Activity vs Sleep Duration', fontsize=12, fontweight='bold')
    plt.xlabel('Physical Activity (minutes)')
    plt.ylabel('Sleep Duration (hours)')
    
    # 6. Stress Level vs Sleep Quality
    plt.subplot(3, 4, 6)
    plt.scatter(df['Stress Level'], df['Quality of Sleep'], alpha=0.6, color='red')
    plt.title('Stress Level vs Sleep Quality', fontsize=12, fontweight='bold')
    plt.xlabel('Stress Level (1-10)')
    plt.ylabel('Sleep Quality (1-10)')
    
    # 7. Age Distribution
    plt.subplot(3, 4, 7)
    plt.hist(df['Age'], bins=15, alpha=0.7, color='lightcoral', edgecolor='black')
    plt.title('Age Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    # 8. Daily Steps Distribution
    plt.subplot(3, 4, 8)
    plt.hist(df['Daily Steps'], bins=20, alpha=0.7, color='lightblue', edgecolor='black')
    plt.title('Daily Steps Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Steps')
    plt.ylabel('Frequency')
    
    # 9. Sleep Duration by Gender
    plt.subplot(3, 4, 9)
    df.boxplot(column='Sleep Duration', by='Gender', ax=plt.gca())
    plt.title('Sleep Duration by Gender', fontsize=12, fontweight='bold')
    plt.suptitle('')  # Remove default title
    
    # 10. Sleep Quality by BMI Category
    plt.subplot(3, 4, 10)
    df.boxplot(column='Quality of Sleep', by='BMI Category', ax=plt.gca())
    plt.title('Sleep Quality by BMI Category', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    plt.suptitle('')  # Remove default title
    
    # 11. Heart Rate Distribution
    plt.subplot(3, 4, 11)
    plt.hist(df['Heart Rate'], bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('Heart Rate Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Heart Rate (BPM)')
    plt.ylabel('Frequency')
    
    # 12. Occupation Distribution
    plt.subplot(3, 4, 12)
    occupation_counts = df['Occupation'].value_counts()
    plt.bar(range(len(occupation_counts)), occupation_counts.values, color='teal', alpha=0.7)
    plt.title('Occupation Distribution', fontsize=12, fontweight='bold')
    plt.xticks(range(len(occupation_counts)), occupation_counts.index, rotation=45)
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('sleep_health_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("   ✅ Visualizations saved as 'sleep_health_analysis.png'")

def generate_insights(df):
    """Generate key insights from the analysis"""
    
    print(f"\n💡 KEY INSIGHTS:")
    
    # Insight 1: Sleep Duration
    avg_sleep = df['Sleep Duration'].mean()
    if avg_sleep < 7:
        print(f"   🚨 CRITICAL: Average sleep duration ({avg_sleep:.1f}h) is below recommended 7-9 hours")
    elif avg_sleep < 8:
        print(f"   ⚠️  WARNING: Average sleep duration ({avg_sleep:.1f}h) is below optimal 8 hours")
    else:
        print(f"   ✅ GOOD: Average sleep duration ({avg_sleep:.1f}h) is within healthy range")
    
    # Insight 2: Sleep Disorders
    disorder_rate = len(df[df['Sleep Disorder'] != 'None']) / len(df) * 100
    print(f"   📊 {disorder_rate:.1f}% of people have sleep disorders")
    
    # Insight 3: Physical Activity
    avg_activity = df['Physical Activity Level'].mean()
    if avg_activity < 30:
        print(f"   ⚠️  Low physical activity levels ({avg_activity:.0f} min/day) - below WHO recommendation of 30 min")
    else:
        print(f"   ✅ Good physical activity levels ({avg_activity:.0f} min/day)")
    
    # Insight 4: Stress Levels
    avg_stress = df['Stress Level'].mean()
    if avg_stress > 7:
        print(f"   🚨 High stress levels ({avg_stress:.1f}/10) - may impact sleep quality")
    elif avg_stress > 5:
        print(f"   ⚠️  Moderate stress levels ({avg_stress:.1f}/10)")
    else:
        print(f"   ✅ Low stress levels ({avg_stress:.1f}/10)")
    
    # Insight 5: BMI Distribution
    obese_rate = len(df[df['BMI Category'] == 'Obese']) / len(df) * 100
    overweight_rate = len(df[df['BMI Category'] == 'Overweight']) / len(df) * 100
    print(f"   ⚖️ {obese_rate:.1f}% obese, {overweight_rate:.1f}% overweight")
    
    # Insight 6: Gender Differences
    male_sleep = df[df['Gender'] == 'Male']['Sleep Duration'].mean()
    female_sleep = df[df['Gender'] == 'Female']['Sleep Duration'].mean()
    print(f"   👨👩 Gender sleep difference: Males {male_sleep:.1f}h vs Females {female_sleep:.1f}h")

def main():
    """Main analysis function"""
    
    # Load and analyze data
    df = load_and_analyze_data()
    
    # Perform various analyses
    analyze_categorical_features(df)
    analyze_sleep_patterns(df)
    analyze_lifestyle_factors(df)
    analyze_correlations(df)
    analyze_by_groups(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate insights
    generate_insights(df)
    
    print(f"\n" + "="*80)
    print("ANALYSIS COMPLETE! 🎉")
    print("="*80)
    
    return df

if __name__ == "__main__":
    df = main()
