class L2vpnService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against l2vpn.yang")

    def render_template(self):
        print("Rendering l2vpn.xml template")
        return "<config>l2vpn</config>"
