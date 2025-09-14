# Sleep Health and Lifestyle Dataset Analysis Report

## 📊 Dataset Overview

- **Total Records**: 374 individuals
- **Total Features**: 13 variables
- **Dataset Shape**: (374, 13)
- **Missing Values**: 219 missing values in Sleep Disorder column (58.6% missing)

## 📋 Dataset Structure

The dataset contains the following variables:

1. **Person ID** - Unique identifier
2. **Gender** - Male/Female distribution
3. **Age** - Age range: 27-59 years
4. **Occupation** - 11 different job categories
5. **Sleep Duration** - Hours of sleep per night
6. **Quality of Sleep** - Self-rated quality (1-10 scale)
7. **Physical Activity Level** - Minutes per day
8. **Stress Level** - Self-rated stress (1-10 scale)
9. **BMI Category** - Weight classification
10. **Blood Pressure** - Systolic/Diastolic readings
11. **Heart Rate** - Resting heart rate (BPM)
12. **Daily Steps** - Steps per day
13. **Sleep Disorder** - Sleep disorder diagnosis

## 🏷️ Demographic Analysis

### Gender Distribution
- **Male**: 189 individuals (50.5%)
- **Female**: 185 individuals (49.5%)
- *Nearly equal gender distribution*

### Age Distribution
- **Average Age**: 42.2 years
- **Age Range**: 27-59 years
- **Standard Deviation**: 8.7 years
- *Middle-aged adult population*

### Occupation Distribution
1. **Nurse**: 73 (19.5%) - Healthcare workers
2. **Doctor**: 71 (19.0%) - Healthcare workers
3. **Engineer**: 63 (16.8%) - Technical professionals
4. **Lawyer**: 47 (12.6%) - Legal professionals
5. **Teacher**: 40 (10.7%) - Education sector
6. **Accountant**: 37 (9.9%) - Financial professionals
7. **Salesperson**: 32 (8.6%) - Sales professionals
8. **Software Engineer**: 4 (1.1%) - Tech professionals
9. **Scientist**: 4 (1.1%) - Research professionals
10. **Sales Representative**: 2 (0.5%) - Sales professionals
11. **Manager**: 1 (0.3%) - Management

*Healthcare workers (Nurses + Doctors) represent 38.5% of the sample*

## 😴 Sleep Health Analysis

### Sleep Duration
- **Average**: 7.13 hours per night
- **Range**: 5.8 - 8.5 hours
- **Standard Deviation**: 0.80 hours
- **Assessment**: ✅ Within recommended 7-9 hour range

### Sleep Quality
- **Average**: 7.31/10
- **Range**: 4 - 9/10
- **Assessment**: ✅ Good overall sleep quality

### Sleep Disorders
- **Total with Disorders**: 155 individuals (41.4%)
- **Sleep Apnea**: 78 cases (20.9%)
- **Insomnia**: 77 cases (20.6%)
- **No Disorder**: 219 cases (58.6%)

*Note: There are 219 missing values in the Sleep Disorder column*

## 🏃 Lifestyle Factors

### Physical Activity
- **Average**: 59.2 minutes per day
- **Range**: 30 - 90 minutes per day
- **Assessment**: ✅ Exceeds WHO recommendation of 30 minutes

### Stress Levels
- **Average**: 5.4/10
- **Range**: 3 - 8/10
- **Assessment**: ⚠️ Moderate stress levels

### Daily Steps
- **Average**: 6,817 steps per day
- **Range**: 3,000 - 10,000 steps
- **Assessment**: ⚠️ Below recommended 10,000 steps

### BMI Distribution
- **Normal**: 195 individuals (52.1%)
- **Overweight**: 148 individuals (39.6%)
- **Normal Weight**: 21 individuals (5.6%)
- **Obese**: 10 individuals (2.7%)

*42.3% of individuals are overweight or obese*

## 🔗 Key Correlations

### Strong Positive Correlations (>0.7)
1. **Sleep Duration ↔ Quality of Sleep**: 0.883
   - *Longer sleep duration strongly correlates with better sleep quality*

2. **Physical Activity ↔ Daily Steps**: 0.773
   - *Higher physical activity correlates with more daily steps*

### Strong Negative Correlations (<-0.7)
1. **Quality of Sleep ↔ Stress Level**: -0.899
   - *Higher stress strongly correlates with worse sleep quality*

2. **Sleep Duration ↔ Stress Level**: -0.811
   - *Higher stress correlates with shorter sleep duration*

### Moderate Correlations
- **Stress Level ↔ Heart Rate**: 0.670
- **Quality of Sleep ↔ Heart Rate**: -0.660
- **Age ↔ Quality of Sleep**: 0.474
- **Age ↔ Stress Level**: -0.422

## 👥 Group-Based Insights

### By Gender
| Metric | Female | Male |
|--------|--------|------|
| Sleep Duration | 7.23h | 7.04h |
| Sleep Quality | 7.66/10 | 6.97/10 |
| Physical Activity | 59.1 min | 59.2 min |
| Stress Level | 4.68/10 | 6.08/10 |
| Daily Steps | 6,841 | 6,794 |

**Key Finding**: Females report better sleep quality and lower stress levels than males.

### By BMI Category
| BMI Category | Sleep Duration | Sleep Quality | Physical Activity | Stress Level | Daily Steps |
|-------------|----------------|---------------|-------------------|--------------|-------------|
| Normal | 7.39h | 7.66/10 | 57.7 min | 5.13/10 | 6,887 |
| Normal Weight | 7.33h | 7.43/10 | 60.3 min | 5.19/10 | 6,767 |
| Overweight | 6.77h | 6.90/10 | 61.2 min | 5.73/10 | 6,966 |
| Obese | 6.96h | 6.40/10 | 55.0 min | 5.70/10 | 3,350 |

**Key Finding**: Normal BMI individuals have better sleep duration and quality.

### By Sleep Disorder
| Disorder | Sleep Duration | Sleep Quality | Physical Activity | Stress Level | Daily Steps |
|----------|----------------|---------------|-------------------|--------------|-------------|
| Insomnia | 6.59h | 6.53/10 | 46.8 min | 5.87/10 | 5,901 |
| Sleep Apnea | 7.03h | 7.21/10 | 74.8 min | 5.67/10 | 7,619 |

**Key Finding**: Sleep Apnea patients have better sleep metrics than Insomnia patients.

## 💡 Key Insights & Recommendations

### 🚨 Critical Findings
1. **High Sleep Disorder Rate**: 41.4% of individuals have diagnosed sleep disorders
2. **Stress-Sleep Connection**: Strong negative correlation (-0.899) between stress and sleep quality
3. **BMI Impact**: Overweight/obese individuals have worse sleep metrics

### ⚠️ Areas of Concern
1. **Moderate Stress Levels**: Average stress level of 5.4/10 may impact sleep quality
2. **Low Daily Steps**: Average 6,817 steps below recommended 10,000
3. **High Overweight Rate**: 39.6% overweight, 2.7% obese

### ✅ Positive Findings
1. **Good Sleep Duration**: Average 7.13 hours within healthy range
2. **High Sleep Quality**: Average 7.31/10 indicates good sleep quality
3. **Adequate Physical Activity**: 59.2 minutes exceeds WHO recommendations
4. **Gender Balance**: Nearly equal male/female distribution

### 📋 Recommendations

#### For Individuals
1. **Stress Management**: Implement stress reduction techniques (meditation, exercise, therapy)
2. **Increase Daily Steps**: Aim for 10,000+ steps per day
3. **Weight Management**: Focus on healthy BMI maintenance
4. **Sleep Hygiene**: Maintain consistent sleep schedule and environment

#### For Healthcare Providers
1. **Sleep Disorder Screening**: Implement routine sleep disorder assessments
2. **Stress Assessment**: Include stress evaluation in health checkups
3. **Lifestyle Counseling**: Provide guidance on physical activity and sleep hygiene
4. **BMI Monitoring**: Regular weight management support

#### For Organizations
1. **Workplace Wellness**: Implement stress management programs
2. **Flexible Schedules**: Allow for better work-life balance
3. **Health Screenings**: Regular health assessments for employees
4. **Education Programs**: Sleep health and lifestyle education

## 📊 Data Quality Notes

- **Missing Data**: 58.6% missing values in Sleep Disorder column
- **Data Completeness**: All other variables have complete data
- **Data Range**: Values appear within realistic ranges
- **Consistency**: Data appears internally consistent

## 🎯 Conclusion

This dataset reveals a population with generally good sleep health but significant stress-related challenges. The strong correlation between stress and sleep quality suggests that stress management should be a primary focus for improving sleep health. The high rate of sleep disorders (41.4%) indicates the need for better screening and treatment programs.

The dataset provides valuable insights for developing targeted interventions to improve sleep health, reduce stress, and promote healthier lifestyles across different demographic groups.
