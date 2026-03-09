class SysrepoClient:
    def __init__(self):
        print("Sysrepo client initialized")

    def load_model(self, yang_file):
        print(f"Loading YANG model: {yang_file}")

    def store_service_instance(self, service_name, xml):
        print(f"Storing XML for {service_name} in Sysrepo")
