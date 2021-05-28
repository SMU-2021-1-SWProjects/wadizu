from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask import jsonify

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/trajectory', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        longtitude = request.json.get('longtitude', None)
        latitude = request.json.get('latitude', None)
        timestamp = request.json.get('timestamp', None)

        db = get_db()
        error = None

        if not longtitude or not latitude or not timestamp:
            error = 'Longtitude, latitude, timestamp is required'
        
        if error is None:
            db.execute(
                'INSERT INTO trajectory (longtitude, latitude, timestamp) VALUES (?, ?, ?)',
                (longtitude, latitude, timestamp)
            )
            db.commit()

            return jsonify({ 'msg': 'trajectory registered' }), 201
        
        return jsonify({ 'msg': error }), 400
    
    db = get_db()
    trajectory = db.execute(
        'SELECT * FROM trajectory'
    ).fetchall()

    json_data=[]
    for result in trajectory:
        json_data.append(dict(zip([i for i in range(len(result))], result)))

    return jsonify(json_data)