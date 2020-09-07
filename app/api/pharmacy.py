from flask_jsonrpc import JSONRPCBlueprint

pharmacy = JSONRPCBlueprint('pharmacy', __name__)


@pharmacy.method('Pharmacy.index')
def index() -> str:
    return 'Welcome to pharmacy API'