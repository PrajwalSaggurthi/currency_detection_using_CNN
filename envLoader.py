from dotenv import dotenv_values

env_tokens = dotenv_values("../.env")

TRAINING_DATA=env_tokens['TRAINING_DATA']
TEST_DATA=env_tokens['TEST_DATA']
VALIDATION_DATA=env_tokens['VALIDATION_DATA']
PREPROCESSED_DATA=env_tokens['PREPROCESSED_DATA']