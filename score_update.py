# score_update.py

import time
from ai_model import ai_model_instance
from database import db_instance
from blockchain import blockchain_instance

class ScoreUpdate:
    def __init__(self):
        self.update_interval = 60  # Update interval in seconds

    def update_scores(self):
        while True:
            # Fetch all users from the database
            users = db_instance.fetch_query("SELECT * FROM users")

            for user in users:
                user_id, user_data = user[0], user[1]

                # Predict the user's authenticity score using the AI model
                score = ai_model_instance.predict(user_data)

                # Update the user's score in the database
                db_instance.execute_query(
                    "UPDATE users SET score = %s WHERE id = %s",
                    (score, user_id)
                )

                # Update the user's score on the blockchain
                blockchain_instance.send_transaction(
                    to_address=user_id,
                    value=score
                )

            # Sleep for the update interval before the next update
            time.sleep(self.update_interval)

score_update_instance = ScoreUpdate()
