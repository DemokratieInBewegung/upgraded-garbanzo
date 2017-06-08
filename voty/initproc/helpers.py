from .models import Initiative
from notifications.signals import notify


def generate_initiative_from_random_wikipedia_article():
    import wikipedia
    wikipedia.set_lang('de')
    article = wikipedia.page(wikipedia.random())
    content = article.content
    chars = int(len(content) / 6)
    Initiative(title=article.title[:80],
               state='i',
               summary=content[0:chars],
               forderung=content[chars:chars*2],
               kosten=content[chars*2:chars*3],
               fin_vorschlag=content[chars*3:chars*4],
               arbeitsweise=content[chars*4:chars*5],
               init_argument=content[chars*5:chars*6]).save()


def notify_initiative_listeners(ini, msg):
    for user in ini.initiators.all():
        notify.send(ini, verb=msg, recipient=user)

    for user in ini.supporters.all():
        notify.send(ini, verb=msg, recipient=user)
