class DeviceService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against device.yang")

    def render_template(self):
        print("Rendering device.xml template")
        return "<config>device</config>"
