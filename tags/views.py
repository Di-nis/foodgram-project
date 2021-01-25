from django.shortcuts import render
import pandas as pd
# from users.forms import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import xlwt

User = get_user_model()


def test(request):
    # Create the HttpResponse object with the appropriate headers.
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="example.xls"'

    # Create the Exel
    workbook = xlwt.Workbook()
    # add data
    # save to buffer
    workbook.save(response)
    return response

# def test(request):
#     id = []
#     username = []
#     users = User.objects.all()
#     for user in User.objects.all():
#         id += [user.id]
#         username += [user.username]

#     d = {'id': id, 'username': username}
#     df = pd.DataFrame(data=d)
#     df.to_excel("output.xlsx")

#     return HttpResponse("Here's the text of the Web page.")
# range1 = [i for i in range(5,15)]
# range2 = [i for i in range(30,67)]
# usecols = range1 + range2

# df = pd.read_csv('C:/Dev/foodgram-project/ingredients/ingredients.csv', delimiter=',', nrows=50)
# df = pd.DataFrame(
#     [id, username]
#     columns=['col 1', 'col 2']
# )

# print(df.sample(5))
# df.to_excel("output.xlsx")
