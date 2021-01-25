# import numpy as np
import pandas as pd
# from users.forms import User
from django.contrib.auth import get_user_model

User = get_user_model()


users = User.objects.get(id=1)

print(users)
# range1 = [i for i in range(5,15)]
# range2 = [i for i in range(30,67)]
# usecols = range1 + range2

# df = pd.read_csv('C:/Dev/foodgram-project/ingredients/ingredients.csv', delimiter=',', nrows=50)


# print(df.sample(5))
# df.to_excel("output.xlsx")