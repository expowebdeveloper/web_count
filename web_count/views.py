from flask import jsonify, request
from flask_restful import Resource,abort
from web_count.models import Website
from web_count.utils import most_common
from web_count import db

class WebsiteView(Resource):
    response = {'status':True,'message':'Request completed successfully'}
    not_found_status = 404
    no_content = 204
    ok_status_code = 200
    created_status_code = 201
    bad_status_code = 400
    already_exist_status_code = 409
    
    def not_found(self):
        response = self.response.copy()
        response['status']=False
        response['message']="Unable to find website"
        abort(self.not_found_status, message=jsonify(response))


    def get(self):
        response = self.response.copy()
        status = self.ok_status_code
        name = request.args.get("name")
        count = request.args.get("count")
        if not any([name,count]):
            response['message']='Please provide atleast one query param (name,count)'
            response['status']=False
            return response,self.bad_status_code
        if count:
            count = int(count)

        if name and count:
            obj = Website.query.filter_by(name=name)
            obj = obj.first()
            if obj:
                data = obj.serialize['content']
                response['data'] = most_common(data,count)
            else:
                self.not_found()

        elif name:
            obj = Website.query.filter_by(name=name)
            obj = obj.first()
            if obj:
                response = obj.serialize
            else:
                self.not_found()

        elif count:
            data = [i.content for i in Website.query.all()]
            if data:
                data = ' '.join(data)
                response = most_common(data,count)

        return response,status

    def post(self,*args,**kwargs):
        response = self.response.copy()
        status = self.created_status_code
        data = request.get_json()
        if not data:
            response['message']="Please provide name and content"
            response['status']=False
            status = self.bad_status_code
        name = data.get('name')
        content = data.get('content')
        if name and content:
            obj = Website.query.filter_by(name=name).first()
            if obj:
                response['message']="Already exist"
                response['status']=False
                status = self.already_exist_status_code
            else:
                obj = Website.create(name=name,content=content)
                response['data']=obj.serialize
        return response, status

    def delete(self,pk):
        response = self.response.copy()
        status = self.no_content
        filter_obj = Website.query.filter_by(id=pk)
        obj = filter_obj.first()
        if obj:
            filter_obj.delete()
            db.session.commit()
        else:
            self.not_found()
        return response,status

    def put(self,pk):
        abort(501)
        response = self.response.copy()
        data = request.get_json()
        filter_obj = Website.query.filter_by(id=pk)
        status = self.ok_status_code
        obj = filter_obj.first()
        if obj:
            Website.update(obj,**data)
        else:
            self.not_found()
        return response,status