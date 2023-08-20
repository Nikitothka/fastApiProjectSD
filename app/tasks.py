from celery import Celery
import time

app = Celery('tasks')
app.config_from_object('celery_config')

@app.task
def generate_image(text_query):
    time.sleep(5)
    print(f"Generated image for query: {text_query}")
