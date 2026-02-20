
from django.core.management.base import BaseCommand
from django.conf import settings
from recommendation.models import Movie
import voyageai
import time

class Command(BaseCommand):
    help = 'Ingest sample movie data and generate embeddings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Connecting to VoyageAI...")
        voyage_client = voyageai.Client(api_key=settings.VOYAGE_API_KEY)
        
        # Sample Data
        sample_movies = [
            {"title": "The Matrix", "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
            {"title": "Inception", "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."},
            {"title": "Interstellar", "plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
            {"title": "The Avengers", "plot": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."},
            {"title": "The Lion King", "plot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself."},
            {"title": "Toy Story", "plot": "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room."},
            {"title": "Pulp Fiction", "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
            {"title": "The Godfather", "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
            {"title": "Forrest Gump", "plot": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75."},
            {"title": "Fight Club", "plot": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into something much, much more."}
        ]

        self.stdout.write(f"Ingesting {len(sample_movies)} movies...")

        plots = [m["plot"] for m in sample_movies]
        
        try:
            self.stdout.write("Generating embeddings...")
            result = voyage_client.embed(plots, model="voyage-large-2")
            
            # Clear existing data first?
            Movie.objects.all().delete()

            movies_to_create = []
            for i, movie_data in enumerate(sample_movies):
                movie = Movie(
                    title=movie_data["title"],
                    plot=movie_data["plot"],
                    embedding=result.embeddings[i]
                )
                movies_to_create.append(movie)
            
            Movie.objects.bulk_create(movies_to_create)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully ingested {len(movies_to_create)} movies!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error during ingestion: {e}"))
