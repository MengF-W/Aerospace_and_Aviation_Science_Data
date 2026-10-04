# def
import requests
import re
from typing import List
from nasaApp.serializers import APODSerializer

class ApodServices:
    @staticmethod
    def get_apod_basic(api_client=requests) -> List:
        result = api_client.get("https://science.nasa.gov/wp-json/wp/v2/apod-basic")
        result_item_list = []

        for item in result.json():

            match item["media_type"]:
                case "image":
                    source = re.findall('<meta property="og:image:secure_url" content=.*>', item["basic_html"])[0]
                    source = re.sub('<meta property=\"og:image:secure_url\" content=', '', source)
                    source = re.sub('>', '', source)
                    item["media_location"] = "<IMG SRC=" + source + "alt="+ item["alt"] + " width=\"200\" height=\"300\">"
                case "video":
                    item["media_location"] = re.findall('<source src=.*.mp4', item["basic_html"])[0] + "\">"

            serializer = APODSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            apod = serializer.data

            result_item_list.append(apod)

        return result_item_list