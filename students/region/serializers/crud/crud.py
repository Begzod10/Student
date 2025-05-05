from students.models.region import Region, District
from students.region.regions import provinces_data, districts_data


def create_regions():
    for province in provinces_data:
        get_region = Region.objects.get(name=province['name_uz'])
        if not get_region:
            Region.objects.get_or_create(
                name=province['name_uz'],
                name_oz=province['name_oz'],
                name_ru=province['name_ru'],
                name_en=province['name_en'],

            )
        else:
            get_region.name_ru = province['name_ru']
            get_region.name_en = province['name_en']
            get_region.save()

    for district in districts_data:
        District.objects.get_or_create(
            name=district['name_uz'],
            name_ru=district['name_ru'],
            name_en=district['name_en'],
            region_id=district['province_id']
        )
