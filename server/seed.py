from app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
import random
from datetime import date, timedelta

def create_seed_data():
    # Clear existing data
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Create 10 users
    users = []
    for i in range(1, 11):
        user = User(username=f'user{i}', password_hash=f'hashed_pass_{i}')
        users.append(user)
        db.session.add(user)
    db.session.commit()
    print("Created 10 users")

    # Create 10 guests
    occupations = [
        'Actor', 'Musician', 'Comedian', 'Writer', 'Director',
        'Politician', 'Athlete', 'Scientist', 'Chef', 'Activist'
    ]
    first_names = ['John', 'Emma', 'Michael', 'Olivia', 'James', 
                  'Sophia', 'Robert', 'Isabella', 'David', 'Mia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
                 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    
    guests = []
    for i in range(10):
        guest = Guest(
            name=f"{first_names[i]} {last_names[i]}",
            occupation=occupations[i]
        )
        guests.append(guest)
        db.session.add(guest)
    db.session.commit()
    print("Created 10 guests")

    # Create 10 episodes
    episodes = []
    start_date = date(2023, 1, 1)
    for i in range(1, 11):
        episode = Episode(
            date=str(start_date + timedelta(days=7*i)),
            number=i
        )
        episodes.append(episode)
        db.session.add(episode)
    db.session.commit()
    print("Created 10 episodes")

    # Create 10 appearances
    for i in range(10):
        appearance = Appearance(
            rating=random.randint(1, 5),
            guest_id=guests[i].id,
            episode_id=episodes[i].id
        )
        db.session.add(appearance)
    db.session.commit()
    print("Created 10 appearances")

if __name__ == '__main__':
    with app.app_context():
        create_seed_data()
        print("Database seeding completed!")