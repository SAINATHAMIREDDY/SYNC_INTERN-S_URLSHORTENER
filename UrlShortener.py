from aurlcutter import Cutter
import asyncio
link=input("ENTER THE LINK:")
async def main(link):
    cutter_instance =Cutter()
    cutted_link =await cutter_instance.tinyurl.cut(link)
    print(cutted_link)
asyncio.run(main(link))
