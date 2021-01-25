
from main.models import *

home_appliances = Category.objects.create(name="Home_appliances")
category = Category.objects.filter(id=3)
category.update(name="Техника для дома")

vacuum_cleaner = Product.objects.create(name='Робот-пылесос', category=category,
                                        description='Роботизированный уборщик из среднего сегмента роботов-пылесосов, '
                                        'который может одновременно пылесосить и мыть полы.', price='150')
vacuum_cleaner.price ='19228'
vacuum_cleaner.save()

tag_3 = Tags.objects.create(name='Робот-пылесос Roborock E4')
vacuum_cleaner.tag.add(2)
# выбрала не верный айди тега
vacuum_cleaner.tag.remove(2)
# удалила не правильный тег
vacuum_cleaner.add(3)
vacuum_cleaner.tag.all()
# <QuerySet [<Tags: Робот-пылесос Roborock E4>]>

