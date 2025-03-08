from flask import Blueprint, request, jsonify # type: ignore

auth_bp = Blueprint("auth", __name__)