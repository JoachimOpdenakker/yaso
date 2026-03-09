class Node_createService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against node_create.yang")

    def render_template(self):
        print("Rendering node_create.xml template")
        return "<config>node_create</config>"
