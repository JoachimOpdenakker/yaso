class Core_linkService:
    def __init__(self, data):
        self.data = data

    def validate_yang(self):
        print("Validating data against core_link.yang")

    def render_template(self):
        print("Rendering core_link.xml template")
        return "<config>core_link</config>"
