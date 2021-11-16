from flask import Response, request
from flask_restful import Resource
from database.prediction_models import PredictionModel
from database.users import User
from database.api_calls import ApiCallTracking
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, ModelAlreadyExistsError, \
InternalServerError, UpdatingModelError, DeletingModelError, ModelNotExistsError



class ModelsApi(Resource):

  @jwt_required()
  def get(self):
    user_id = get_jwt_identity()
    track_api_call(api_name="getModelsAPI", user_id=user_id, prediction_model_id=None)
    user = User.objects.get(id=user_id)
    model = PredictionModel.objects(added_by = user).to_json()
    return Response(model, mimetype="application/json", status=200)

  @jwt_required()
  def post(self):
      try:
        user_id = get_jwt_identity()
        track_api_call(api_name="postModelsAPI", user_id=user_id, prediction_model_id=None)
        body = request.get_json()
        user = User.objects.get(id=user_id)
        model = PredictionModel(**body, added_by=user)
        model.save()
        user.update(push__prediction_models = model)
        user.save()
        id = model.id
        return {'id': str(id)}, 200
      except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
      except NotUniqueError:
        raise ModelAlreadyExistsError
      except Exception as e:
        raise InternalServerError

class ModelApi(Resource):

  @jwt_required()
  def put(self, id):
    try:
      user_id = get_jwt_identity()
      track_api_call(api_name="putModelAPI", user_id=user_id, prediction_model_id=None)
      model = PredictionModel.objects.get(id=id, added_by=user_id)
      body = request.get_json()
      PredictionModel.objects.get(id=id).update(**body)

      return '', 200

    except InvalidQueryError:

      raise SchemaValidationError

    except DoesNotExist:

      raise UpdatingModelError

    except Exception:

      raise InternalServerError

  @jwt_required()
  def delete(self, id):

    try:
      user_id = get_jwt_identity()
      track_api_call(api_name="deleteModelAPI", user_id=user_id, prediction_model_id=None)
      model = PredictionModel.objects.get(id=id, added_by=user_id)
      model.delete()

      return '', 200
    except DoesNotExist:

      raise DeletingModelError
    except Exception:

      raise InternalServerError

  @jwt_required()
  def get(self, id):

    try:
      user_id = get_jwt_identity()
      track_api_call(api_name="getModelAPI", user_id=user_id,  prediction_model_id=None)
      model = PredictionModel.objects.get(id=id).to_json()

      return Response(model, mimetype="application/json", status=200)
    except DoesNotExist:

      raise ModelNotExistsError
    except Exception:

      raise InternalServerError

class ExecuteModelApi(Resource):
    @jwt_required()
    def post(self, id):
        try:
            user_id = get_jwt_identity()
            track_api_call(api_name="postExecuteModelAPI", user_id=user_id, prediction_model_id=id)
            model = PredictionModel.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            # check for correct input length in order to make it more secure and also define an appropriate exception
            output = model.execute(body["model_parameter"])
            return {'output': float(output)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ModelAlreadyExistsError
        except Exception as e:
            raise InternalServerError


def track_api_call(api_name, user_id, prediction_model_id):
        now = datetime.now()
        tracking_object = ApiCallTracking(api_name= api_name, date=now, called_by=user_id, model_called=prediction_model_id)
        tracking_object.save()

