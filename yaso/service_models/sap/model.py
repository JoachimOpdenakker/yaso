class SapService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against sap.yang")

    def render_template(self):
        print("Rendering sap.xml template")
        return "<config>sap</config>"
