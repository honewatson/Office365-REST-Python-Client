from office365.runtime.client_object_collection import ClientObjectCollection
from office365.runtime.queries.service_operation_query import ServiceOperationQuery
from office365.runtime.resource_path_service_operation import ResourcePathServiceOperation
from office365.sharepoint.recyclebin.recycleBinItem import RecycleBinItem


class RecycleBinItemCollection(ClientObjectCollection):
    """Represents a collection of View resources."""

    def __init__(self, context, resource_path=None):
        super(RecycleBinItemCollection, self).__init__(context, RecycleBinItem, resource_path)

    def move_all_to_second_stage(self):
        qry = ServiceOperationQuery(self, "MoveAllToSecondStage")
        self.context.add_query(qry)
        return self

    def get_by_id(self, recycleBinId):
        """
        Returns the recycle bin type with the given identifier from the collection.

        :param str recycleBinId: A hexadecimal value representing the identifier of a recycle bin.
        """
        return RecycleBinItem(self.context,
                              ResourcePathServiceOperation("GetById", [recycleBinId], self.resource_path))

    def delete_all(self):
        """Permanently deletes all Recycle Bin items."""
        qry = ServiceOperationQuery(self, "DeleteAll")
        self.context.add_query(qry)
        return self

    def restore_all(self):
        """Restores all Recycle Bin items to their original locations."""
        qry = ServiceOperationQuery(self, "RestoreAll")
        self.context.add_query(qry)
        return self
