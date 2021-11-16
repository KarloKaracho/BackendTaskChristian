from .prediction_models_api import ModelsApi, ModelApi,ExecuteModelApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
 api.add_resource(ExecuteModelApi, '/api/execute_model/<id>')
 api.add_resource(ModelsApi, '/api/edit_models')
 api.add_resource(ModelApi, '/api/edit_models/<id>')
 api.add_resource(SignupApi, '/api/auth/signup')
 api.add_resource(LoginApi, '/api/auth/login')
 api.add_resource(ForgotPassword, '/api/auth/forgot')
 api.add_resource(ResetPassword, '/api/auth/reset')