class PortService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against port.yang")

    def render_template(self):
        print("Rendering port.xml template")
        return "<config>port</config>"
