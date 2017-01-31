# -*- coding: utf-8 -*-

# qidata
from qidata import makeMetadataObject

# local
from ..datacontroller import DataController

class ImageController(DataController):

    # ───────────
    # Constructor

    def __init__(self, source_path, user_name):
        super(ImageController, self).__init__(source_path, user_name)

    # ─────
    # Slots

    def createNewItem(self, center_coordinates):
        if center_coordinates is not None:
            x=center_coordinates[0]
            y=center_coordinates[1]

            # Create the new object as required
            new_object = [makeMetadataObject(self.last_selected_item_type),[[x-30,y-30],[x+30,y+30]]]

        else:
            # Create the new object as required
            new_object = [makeMetadataObject(self.last_selected_item_type),None]

        # Add it to local and general model
        self.local_model.append(new_object)
        self.model[str(self.last_selected_item_type)].append(new_object)

        # Display it in the image widget
        r = self.addAnnotationItemOnView(new_object[1])

        # Display information on it in data editor widget
        r.select()