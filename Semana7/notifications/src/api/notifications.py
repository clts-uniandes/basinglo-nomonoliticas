from http import HTTPStatus
from src.seedwork.presentation.api import create_blueprint


notification_bp = create_blueprint("notifications", "/notifications")

@notification_bp.route('', methods=['GET'])
def check_health():
    return {"status": "ok"}, HTTPStatus.OK