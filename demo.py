# Quick Demo Script - Enhanced Gift Recommender
# This demonstrates the improvements made in Phase 1 of the development plan

import os
from db import init_db, save_recommendation, get_recommendations, get_database_stats

def demo_database_functionality():
    """Demonstrate the new database capabilities."""
    print("🎁 Gift Recommender - Database Demo")
    print("="*50)
    
    # Initialize database
    print("1. Initializing database...")
    init_db()
    
    # Show current stats
    stats = get_database_stats()
    print(f"2. Current database stats:")
    print(f"   - Total recommendations: {stats['total_recommendations']}")
    print(f"   - Today's recommendations: {stats['today_recommendations']}")
    print(f"   - Most recent: {stats['most_recent_date']}")
    
    # Simulate saving some recommendations
    print("\n3. Adding sample recommendations...")
    
    sample_recommendations = [
        {
            "person_info": "25-year-old yoga instructor who loves plants and healthy living",
            "gift_idea": "A beautiful bamboo yoga block set with carrying case - perfect for enhancing any yoga practice while staying eco-friendly!",
            "product_link": "https://example.com/bamboo-yoga-blocks"
        },
        {
            "person_info": "45-year-old dad who enjoys grilling and craft beer",
            "gift_idea": "A premium BBQ spice rub collection with beer pairing guide - elevate every grilling session with gourmet flavors!",
            "product_link": "https://example.com/bbq-spice-collection"
        },
        {
            "person_info": "22-year-old college student studying computer science",
            "gift_idea": "A mechanical keyboard with customizable RGB lighting - perfect for coding marathons and gaming sessions!",
            "product_link": "https://example.com/gaming-keyboard"
        }
    ]
    
    for i, rec in enumerate(sample_recommendations, 1):
        rec_id = save_recommendation(
            rec["person_info"], 
            rec["gift_idea"], 
            rec["product_link"]
        )
        print(f"   ✓ Saved recommendation {i} (ID: {rec_id})")
    
    # Show updated stats
    print("\n4. Updated database stats:")
    updated_stats = get_database_stats()
    print(f"   - Total recommendations: {updated_stats['total_recommendations']}")
    print(f"   - Today's recommendations: {updated_stats['today_recommendations']}")
    
    # Show recent recommendations
    print("\n5. Recent recommendations:")
    recent_recs = get_recommendations(3)
    for rec in recent_recs:
        rec_id, person_info, gift_idea, product_link, created_at = rec
        print(f"\n   ID: {rec_id} | Created: {created_at}")
        print(f"   Person: {person_info[:60]}...")
        print(f"   Gift: {gift_idea[:80]}...")
        print(f"   Link: {product_link}")
    
    print("\n" + "="*50)
    print("✅ Database functionality demo complete!")
    print("\nNext steps (from DEVELOPMENT_PLAN.md):")
    print("- Add error handling for API failures")
    print("- Set up testing framework with pytest")  
    print("- Add price filtering to recommendations")
    print("- Implement occasion-based recommendations")

def demo_error_handling():
    """Demonstrate improved error handling."""
    print("\n🛡️  Error Handling Demo")
    print("="*50)
    
    # Check if OpenAI API key is set
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("⚠️  OpenAI API key not found in environment variables")
        print("   This demonstrates graceful handling of missing configuration")
        print("   In production, the app would show a user-friendly error message")
    else:
        print("✅ OpenAI API key found - ready for recommendations")
    
    # Demonstrate database error handling
    try:
        # This would normally connect to the database
        stats = get_database_stats()
        print(f"✅ Database connection successful - {stats['total_recommendations']} recommendations stored")
    except Exception as e:
        print(f"⚠️  Database error handled gracefully: {e}")
    
    print("\n" + "="*50)
    print("✅ Error handling demo complete!")

if __name__ == "__main__":
    # Run the demos
    demo_database_functionality()
    demo_error_handling()
    
    print("\n🚀 Ready for Phase 2 development!")
    print("See DEVELOPMENT_PLAN.md for complete roadmap and next steps.")