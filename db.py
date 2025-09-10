# db.py - Database module for gift recommendations

import sqlite3
import os
from datetime import datetime

DATABASE_PATH = "gift_recommendations.db"

def init_db():
    """Initialize the SQLite database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create recommendations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_info TEXT NOT NULL,
            gift_idea_and_pitch TEXT NOT NULL,
            product_link TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def save_recommendation(person_info, gift_idea_and_pitch, product_link):
    """Save a gift recommendation to the database."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO recommendations (person_info, gift_idea_and_pitch, product_link)
            VALUES (?, ?, ?)
        ''', (person_info, gift_idea_and_pitch, product_link))
        
        conn.commit()
        recommendation_id = cursor.lastrowid
        conn.close()
        
        print(f"Recommendation saved with ID: {recommendation_id}")
        return recommendation_id
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def get_recommendations(limit=10):
    """Retrieve recent recommendations from the database."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, person_info, gift_idea_and_pitch, product_link, created_at
            FROM recommendations
            ORDER BY created_at DESC
            LIMIT ?
        ''', (limit,))
        
        recommendations = cursor.fetchall()
        conn.close()
        
        return recommendations
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def search_recommendations(search_term, limit=10):
    """Search recommendations by person info or gift idea."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        search_pattern = f"%{search_term}%"
        cursor.execute('''
            SELECT id, person_info, gift_idea_and_pitch, product_link, created_at
            FROM recommendations
            WHERE person_info LIKE ? OR gift_idea_and_pitch LIKE ?
            ORDER BY created_at DESC
            LIMIT ?
        ''', (search_pattern, search_pattern, limit))
        
        recommendations = cursor.fetchall()
        conn.close()
        
        return recommendations
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_database_stats():
    """Get basic statistics about the recommendations database."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Total recommendations
        cursor.execute('SELECT COUNT(*) FROM recommendations')
        total_count = cursor.fetchone()[0]
        
        # Today's recommendations
        cursor.execute('''
            SELECT COUNT(*) FROM recommendations 
            WHERE DATE(created_at) = DATE('now')
        ''')
        today_count = cursor.fetchone()[0]
        
        # Most recent recommendation
        cursor.execute('''
            SELECT created_at FROM recommendations 
            ORDER BY created_at DESC LIMIT 1
        ''')
        most_recent = cursor.fetchone()
        most_recent_date = most_recent[0] if most_recent else None
        
        conn.close()
        
        return {
            'total_recommendations': total_count,
            'today_recommendations': today_count,
            'most_recent_date': most_recent_date
        }
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {
            'total_recommendations': 0,
            'today_recommendations': 0,
            'most_recent_date': None
        }

if __name__ == "__main__":
    # Test the database functions
    print("Testing database functionality...")
    
    # Initialize database
    init_db()
    
    # Get stats
    stats = get_database_stats()
    print(f"Database stats: {stats}")
    
    # Test saving a recommendation
    test_person_info = "30-year-old software engineer who loves coffee and coding"
    test_gift_idea = "A premium mechanical keyboard with RGB lighting - perfect for long coding sessions and adds personality to any workspace!"
    test_product_link = "https://example.com/mechanical-keyboard"
    
    recommendation_id = save_recommendation(test_person_info, test_gift_idea, test_product_link)
    
    if recommendation_id:
        print(f"Test recommendation saved successfully!")
        
        # Test retrieving recommendations
        recent_recommendations = get_recommendations(5)
        print(f"Found {len(recent_recommendations)} recent recommendations")
        
        # Test searching
        search_results = search_recommendations("coffee", 5)
        print(f"Found {len(search_results)} recommendations matching 'coffee'")
        
        # Updated stats
        updated_stats = get_database_stats()
        print(f"Updated database stats: {updated_stats}")
    
    print("Database testing completed!")