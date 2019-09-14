


def qw:
    import models

    from models import Post
    from app import db
    db.create_all()
    p = Post (title ='First post', body='First post body')
    db.session.add(p)
    db.session.commit()
