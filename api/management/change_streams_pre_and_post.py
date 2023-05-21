import asyncio

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
<<<<<<< HEAD

=======
>>>>>>> adding triggers for catalog data sync
from api.config import get_settings
from api.models.user import Submission


async def main():
    settings = get_settings()
    db = AsyncIOMotorClient(settings.db_connection_string)
    await init_beanie(database=db[settings.database_name], document_models=[Submission])
    # https://www.mongodb.com/docs/manual/reference/command/collMod/#change-streams-with-document-pre--and-post-images
    # This enables us to get the record id of a deleted submission within a trigger.  We need this for removing
    # discovery records when a submission is deleted
    await db[settings.database_name].command(
<<<<<<< HEAD
        ({'collMod': Submission.get_collection_name(), "changeStreamPreAndPostImages": {'enabled': True}})
    )
    db.close()


=======
        ({'collMod': Submission.get_collection_name(), "changeStreamPreAndPostImages": {'enabled': True}}))
    db.close()

>>>>>>> adding triggers for catalog data sync
if __name__ == "__main__":
    asyncio.run(main())
