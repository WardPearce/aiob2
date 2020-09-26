import typing

from ..base import BaseBucket

from ...models.bucket import BucketModel
from ...models.file import FileModel

from .file import BlockingFile

from ...settings import FileSettings


class BlockingBucket(BaseBucket):
    def file_versions(self, settings: FileSettings = None
                      ) -> typing.Generator[typing.Any, None, None]:
        """Used to list file by version.

        Parameters
        ----------
        settings : FileSettings, optional
            by default None

        Yields
        -------
        FileModel
            Holds details on file.
        BlockingFile
        str
            Next file name.
        str
            Next file ID.
        """

        json = {
            "bucketId": self.bucket_id,
        }

        if settings:
            json = {
                **json,
                **settings.payload
            }

        data = self.context._post(
            url=self.context._routes.file.versions,
            json=json,
            include_account=False
        )

        for file in data["files"]:
            yield FileModel(file), self.file(file["fileId"]), \
                file["nextFileName"], file["nextFileId"]

    def file_names(self, settings: FileSettings = None
                   ) -> typing.Generator[typing.Any, None, None]:
        """Used to list file by name.

        Parameters
        ----------
        settings : FileSettings, optional
            by default None

        Yields
        -------
        FileModel
            Holds details on file.
        BlockingFile
        str
            Next file name.
        """

        json = {
            "bucketId": self.bucket_id,
        }

        if settings:
            json = {
                **json,
                **settings.payload
            }

        data = self.context._post(
            url=self.context._routes.file.names,
            json=json,
            include_account=False
        )

        for file in data["files"]:
            yield FileModel(file), self.file(file["fileId"]), \
                file["nextFileName"]

    def file(self, file_id: str) -> BlockingFile:
        """Used to interact with a file.

        Parameters
        ----------
        file_id : str
            ID of a file.

        Returns
        -------
        BlockingFile
        """

        return BlockingFile(self.context, self.bucket_id, file_id)

    def delete(self) -> BucketModel:
        """Used to delete a bucket.

        Returns
        -------
        BucketModel
            Holds details on delete bucked.
        """

        return BucketModel(self.context._post(
            url=self.context._routes.bucket.delete,
            json={
                "bucketId": self.bucket_id
            }
        ))
