<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 4.1.1 on 2022-09-16 02:10
=======
# Generated by Django 4.1.1 on 2022-09-16 02:17
>>>>>>> 86fecf2 (Fix game api ver_0.5)
=======
# Generated by Django 4.1 on 2022-09-19 04:41
>>>>>>> f807105 (fix: makemigrations 다시)
=======
# Generated by Django 4.1.1 on 2022-09-16 05:21
>>>>>>> 91db506 (feat : 회원정보수정)
=======
# Generated by Django 4.1.1 on 2022-09-19 04:16
>>>>>>> 5784305 (Add ToonBTI views.py/question definition)
=======
# Generated by Django 4.1 on 2022-09-19 08:52
>>>>>>> d2a7f0d (fix: makemigrations 재가동)
=======
# Generated by Django 4.1.1 on 2022-09-20 06:37
>>>>>>> f81c1cd (fix: 회원 로그인/로그아웃 등 수정)
=======
# Generated by Django 4.1.1 on 2022-09-19 08:01
>>>>>>> 2711023 (feat: 웹툰 찜 기능 구현 (50%))
=======
# Generated by Django 4.1.1 on 2022-09-22 08:48
>>>>>>> c4b2854 (feat: 웹툰 이미지 검색 api 구현)
=======
# Generated by Django 4.1.1 on 2022-09-26 07:50
>>>>>>> c9803bc (fix : profile 수정, email,nickname 중복확인 수정)
=======
# Generated by Django 4.1.1 on 2022-09-27 01:49
>>>>>>> c5812ab (feat : rating model추가, rating views 수정)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5784305 (Add ToonBTI views.py/question definition)
    dependencies = [
    ]
=======
    dependencies = []
>>>>>>> c4b2854 (feat: 웹툰 이미지 검색 api 구현)

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
<<<<<<< HEAD
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
<<<<<<< HEAD
<<<<<<< HEAD
=======
    dependencies = []
=======
    dependencies = [
    ]
>>>>>>> f81c1cd (fix: 회원 로그인/로그아웃 등 수정)
=======
    dependencies = []
>>>>>>> c5812ab (feat : rating model추가, rating views 수정)

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
<<<<<<< HEAD
<<<<<<< HEAD
=======
    dependencies = []
=======
    dependencies = [
    ]
>>>>>>> c9803bc (fix : profile 수정, email,nickname 중복확인 수정)

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
<<<<<<< HEAD
>>>>>>> 91db506 (feat : 회원정보수정)
=======
>>>>>>> c4b2854 (feat: 웹툰 이미지 검색 api 구현)
=======
>>>>>>> c5812ab (feat : rating model추가, rating views 수정)
                ("question_id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=200)),
                ("option1", models.CharField(max_length=100)),
                ("option2", models.CharField(max_length=100)),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86fecf2 (Fix game api ver_0.5)
=======
>>>>>>> f807105 (fix: makemigrations 다시)
=======
>>>>>>> 91db506 (feat : 회원정보수정)
=======
>>>>>>> 5784305 (Add ToonBTI views.py/question definition)
=======
=======
>>>>>>> c9803bc (fix : profile 수정, email,nickname 중복확인 수정)
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
<<<<<<< HEAD
>>>>>>> f81c1cd (fix: 회원 로그인/로그아웃 등 수정)
=======
>>>>>>> c4b2854 (feat: 웹툰 이미지 검색 api 구현)
=======
>>>>>>> c9803bc (fix : profile 수정, email,nickname 중복확인 수정)
=======
>>>>>>> c5812ab (feat : rating model추가, rating views 수정)
            ],
        ),
    ]
