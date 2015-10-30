
# Import flask dependencies
from flask import Blueprint, request,  jsonify
import json
from app import _db_utils

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_vendor = Blueprint('vendor', __name__, url_prefix='/vendor')

@app_vendor.route('/', methods=['GET'])
def show_all_jobs():
    a = """term = request.args.get('term')
    limit = request.args.get('limit')
    
    terms = term.split(" ")
    orFilter = []
    for item in terms:
        orFilter.append(Job.job_title.like('%%%s%%'  % item ))
    #print or_(*orFilter)
    
    objects = db.session.query(Job,Category,Nest).filter(Job.category_id == Category.id).filter(Job.nest_id == Nest.id).filter(or_(*orFilter)).limit(int(limit))
    job_list = []
    for aa,bb,cc in objects:
        job_list.append(dict(id = aa.id,
                             title = aa.job_title,
                             category_name = bb.name,
                             nest_name = cc.name))
        
    return jsonify(dict(result = job_list))"""
    _db_utils.get_vendor(1);
    return "show all"

# Set the route and accepted methods
@app_vendor.route('/<vendor_id>', methods=['GET'])
def show_vendor_detail(vendor_id):
    
    _db_utils.get_vendor(1);
    job_object = """Job.query.get(job_id);
   
    
    image_list = []
    for image in job_object.images.all():        
        image_list.append(dict(image_path = image.image_path))
    
    job_detail = dict(job_title = job_object.job_title,
                      job_desc = job_object.job_desc,
                      
                      images = image_list)
    
    
    
    return jsonify(job_detail)"""
    return "return one" 
                

