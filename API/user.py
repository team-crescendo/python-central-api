from engine import SingleWebPage
from db import PostgreSQL
from settings import Config


class Users:
    def __init__(self, engine, path="./pages/rank"):
        self.engine = engine

        # self.db = PostgreSQL(**Config().get("APIDatabase"))

        self.parent = SingleWebPage(
            name="/users",
            url_prefix="/users",
            description="Users (유저관리)",
            template_folder=path
        )

        @self.parent.bp.route("/", methods=["POST"])
        def root(*args, **kwargs):
            return "Yes! you're here via POST"

    def is_debugging(self):
        return self.engine.app.debug

def setup(engine):
    engine.register_blueprint(Users(engine).parent.bp)
