from service.app import *
# print(config.BASE_DIR)

if __name__ == '__main__':
    from db_sqlalchemy import db
    db.init_app(app)
    app.run(port=8401, debug=True)




