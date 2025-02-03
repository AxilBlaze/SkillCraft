from flask import current_app
from datetime import datetime, timedelta
import pandas as pd
from app.services.vector_store import get_vector_store

def get_performance_metrics(user_id, time_range='month'):
    """Calculate user's performance metrics over time."""
    
    def calculate_time_range():
        now = datetime.utcnow()
        if time_range == 'week':
            return now - timedelta(days=7)
        elif time_range == 'year':
            return now - timedelta(days=365)
        return now - timedelta(days=30)  # month default
    
    try:
        start_date = calculate_time_range()
        
        # Get user's activity data
        activities = list(current_app.db.user_activities.find({
            'user_id': user_id,
            'timestamp': {'$gte': start_date}
        }))
        
        # Calculate metrics
        metrics = {
            'completion_rate': calculate_completion_rate(activities),
            'accuracy': calculate_accuracy(activities),
            'time_spent': calculate_time_spent(activities),
            'progress_trend': calculate_progress_trend(activities),
            'engagement_score': calculate_engagement_score(activities)
        }
        
        return metrics
    except Exception as e:
        print(f"Error calculating performance metrics: {str(e)}")
        return None

def get_skills_progress(user_id):
    """Analyze and return user's skills progress."""
    try:
        # Get user's completed skills and assessments
        skills = list(current_app.db.user_skills.find({'user_id': user_id}))
        assessments = list(current_app.db.assessment_results.find({'user_id': user_id}))
        
        # Calculate progress by category
        categories = {}
        for skill in skills:
            category = skill.get('category')
            if category not in categories:
                categories[category] = {
                    'total': 0,
                    'completed': 0,
                    'proficiency': 0
                }
            categories[category]['total'] += 1
            if skill.get('status') == 'completed':
                categories[category]['completed'] += 1
                categories[category]['proficiency'] += skill.get('proficiency', 0)
        
        # Get recent achievements
        recent_achievements = get_recent_achievements(user_id)
        
        return {
            'overall': calculate_overall_progress(skills),
            'categories': categories,
            'recent_achievements': recent_achievements
        }
    except Exception as e:
        print(f"Error calculating skills progress: {str(e)}")
        return None

def get_learning_patterns(user_id):
    """Analyze user's learning patterns and behaviors."""
    try:
        # Get user's learning sessions
        sessions = list(current_app.db.learning_sessions.find({'user_id': user_id}))
        
        # Convert to pandas DataFrame for analysis
        df = pd.DataFrame(sessions)
        
        # Analyze patterns
        study_patterns = {
            'peak_hours': analyze_peak_hours(df),
            'session_duration': analyze_session_duration(df),
            'frequency': analyze_frequency(df)
        }
        
        engagement_metrics = calculate_engagement_metrics(df)
        preferred_times = analyze_preferred_times(df)
        
        return {
            'study_patterns': study_patterns,
            'engagement': engagement_metrics,
            'preferred_times': preferred_times
        }
    except Exception as e:
        print(f"Error analyzing learning patterns: {str(e)}")
        return None

def get_improvement_suggestions(user_id):
    """Generate personalized improvement suggestions."""
    try:
        # Get user's performance data
        performance = get_performance_metrics(user_id)
        skills_progress = get_skills_progress(user_id)
        
        # Identify areas for improvement
        weak_areas = identify_weak_areas(skills_progress)
        
        # Generate recommendations
        recommendations = generate_recommendations(weak_areas)
        
        # Find relevant resources
        resources = find_relevant_resources(weak_areas)
        
        return {
            'recommendations': recommendations,
            'focus_areas': weak_areas,
            'resources': resources
        }
    except Exception as e:
        print(f"Error generating improvement suggestions: {str(e)}")
        return None

# Helper functions for calculations and analysis
def calculate_completion_rate(activities):
    """Calculate completion rate from activities."""
    if not activities:
        return 0
    completed = sum(1 for a in activities if a.get('status') == 'completed')
    return (completed / len(activities)) * 100

def calculate_accuracy(activities):
    """Calculate accuracy from assessment activities."""
    assessment_activities = [a for a in activities if a.get('type') == 'assessment']
    if not assessment_activities:
        return 0
    total_score = sum(a.get('score', 0) for a in assessment_activities)
    return total_score / len(assessment_activities)

def calculate_time_spent(activities):
    """Calculate total time spent in learning activities."""
    if not activities:
        return 0
    return sum(activity.get('duration', 0) for activity in activities)

def calculate_progress_trend(activities):
    """Calculate progress trend over time."""
    if not activities:
        return []
    # Sort activities by date and calculate cumulative progress
    sorted_activities = sorted(activities, key=lambda x: x.get('timestamp', 0))
    cumulative_progress = []
    total = 0
    for activity in sorted_activities:
        total += activity.get('progress', 0)
        cumulative_progress.append({
            'date': activity.get('timestamp'),
            'progress': total
        })
    return cumulative_progress

def calculate_engagement_score(activities):
    """Calculate engagement score based on activity frequency and quality."""
    if not activities:
        return 0
    
    activity_frequency = len(activities)
    activity_quality = sum(a.get('engagement_value', 1) for a in activities)
    
    max_frequency = 100  # Arbitrary max for normalization
    frequency_score = min(activity_frequency / max_frequency, 1)
    quality_score = activity_quality / (activity_frequency * 2)  # Assume max quality is 2
    
    return (frequency_score + quality_score) / 2 * 100 

def calculate_overall_progress(skills):
    """Calculate overall progress across all skills."""
    if not skills:
        return 0
    completed = sum(1 for skill in skills if skill.get('status') == 'completed')
    return (completed / len(skills)) * 100 if skills else 0 

def get_recent_achievements(user_id):
    """Get user's recent achievements."""
    try:
        # Get achievements from last 30 days
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        achievements = list(current_app.db.user_achievements.find({
            'user_id': user_id,
            'timestamp': {'$gte': thirty_days_ago}
        }).sort('timestamp', -1).limit(5))
        
        return achievements
    except Exception as e:
        print(f"Error getting recent achievements: {str(e)}")
        return [] 

def analyze_peak_hours(df):
    """Analyze peak study hours from learning sessions."""
    try:
        if df.empty:
            return []
        # Convert timestamp to hour and count sessions per hour
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        peak_hours = df['hour'].value_counts().head(3).index.tolist()
        return peak_hours
    except Exception as e:
        print(f"Error analyzing peak hours: {str(e)}")
        return []

def analyze_session_duration(df):
    """Analyze average session duration."""
    try:
        if df.empty:
            return 0
        return df['duration'].mean()
    except Exception as e:
        print(f"Error analyzing session duration: {str(e)}")
        return 0

def analyze_frequency(df):
    """Analyze learning session frequency."""
    try:
        if df.empty:
            return 0
        # Count unique days with sessions
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        return len(df['date'].unique())
    except Exception as e:
        print(f"Error analyzing frequency: {str(e)}")
        return 0 

def calculate_engagement_metrics(df):
    """Calculate various engagement metrics from learning sessions."""
    try:
        if df.empty:
            return {}
        return {
            'total_sessions': len(df),
            'avg_duration': df['duration'].mean(),
            'completion_rate': (df['status'] == 'completed').mean() * 100,
            'active_days': len(df['timestamp'].dt.date.unique())
        }
    except Exception as e:
        print(f"Error calculating engagement metrics: {str(e)}")
        return {} 

def identify_weak_areas(skills_progress):
    """Identify areas where user needs improvement."""
    try:
        weak_areas = []
        for category, data in skills_progress.get('categories', {}).items():
            if data.get('proficiency', 0) < 70:  # Threshold for weak areas
                weak_areas.append({
                    'category': category,
                    'current_level': data.get('proficiency', 0),
                    'target_level': 70
                })
        return sorted(weak_areas, key=lambda x: x['current_level'])
    except Exception as e:
        print(f"Error identifying weak areas: {str(e)}")
        return [] 

def generate_recommendations(weak_areas):
    """Generate personalized recommendations based on weak areas."""
    try:
        recommendations = []
        for area in weak_areas:
            recommendations.append({
                'category': area['category'],
                'suggestion': f"Focus on improving {area['category']} skills",
                'target_improvement': area['target_level'] - area['current_level'],
                'priority': 'high' if area['current_level'] < 50 else 'medium'
            })
        return recommendations
    except Exception as e:
        print(f"Error generating recommendations: {str(e)}")
        return [] 

def find_relevant_resources(weak_areas):
    """Find learning resources relevant to user's weak areas."""
    try:
        resources = []
        for area in weak_areas:
            # Find resources from database matching the category
            category_resources = list(current_app.db.learning_resources.find({
                'category': area['category'],
                'level': 'beginner' if area['current_level'] < 30 else 'intermediate'
            }).limit(3))
            resources.extend(category_resources)
        return resources
    except Exception as e:
        print(f"Error finding relevant resources: {str(e)}")
        return [] 

def analyze_preferred_times(df):
    """Analyze user's preferred learning times."""
    try:
        if df.empty:
            return {}
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['weekday'] = pd.to_datetime(df['timestamp']).dt.day_name()
        return {
            'peak_hours': df['hour'].value_counts().head(3).index.tolist(),
            'preferred_days': df['weekday'].value_counts().head(3).index.tolist(),
            'most_productive_time': df.groupby('hour')['duration'].mean().idxmax()
        }
    except Exception as e:
        print(f"Error analyzing preferred times: {str(e)}")
        return {} 