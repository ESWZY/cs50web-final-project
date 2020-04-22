from django.test import TestCase
from django.db.models import Q
from .models import Article


# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        # Create articles
        Article.objects.create(title="Ask a Designer: Improving your home's function as refuge",
                               author="MR",
                               date="Today",
                               brief="When your entire life is happening inside your home",
                               free_text="When your entire life is happening inside your home, it matters how that space feels and functions.",
                               pay_text="Interior designers often focused on this even before self-quarantine, asking clients...")
        Article.objects.create(title="No prom? For this teen, it's a trifecta of missed milestones",
                               author="TL",
                               date="2020-04-22 05:41:50",
                               brief="On a Friday night in late February, 17-year-old Amanda Reynolds raced into a department store on Florida's Gulf coast. ",
                               free_text="ST. PETERSBURG, Fla. (AP) — On a Friday night in late February, 17-year-old Amanda Reynolds raced into a department store on Florida's Gulf coast. ",
                               pay_text="She'd been on a mission for weeks, and after...")
        Article.objects.create(title="Pandemic won't cause euro debt crisis, but a North-South divide",
                               author="Jan Strupczewski",
                               date="2020-04-22 06:12:55",
                               brief="Euro zone government debt will surge this year on the coronavirus pandemic",
                               free_text="Euro zone government debt will surge this year on the coronavirus pandemic, but while another debt crisis is unlikely, large differences in indebtedness",
                               pay_text="As countries emerge from the downturn could seriously test their unity.")
        Article.objects.create(title="Patients who continue to shed virus puzzle experts",
                               author="None",
                               date="2020-04-22 HKT 14:17",
                               brief="Dressed in a hazmat suit, two masks and a face shield, Du Mingjun knocked on the mahogany door of a flat in a suburban district of Wuhan on a recent morning.",
                               free_text="<p>Dressed in a hazmat suit, two masks and a face shield, Du Mingjun knocked on the mahogany door of a flat in a suburban district of Wuhan on a recent morning.</p>"
                                         "<p>A man wearing a single mask opened the door a crack and, after Du introduced herself as a psychological counsellor, burst into tears.</p>",
                               pay_text='''<p>'I really can't take it anymore," he said. Diagnosed with the novel coronavirus in early February, the man, who appeared to be in his 50s, had been treated at two hospitals before being transferred to a quarantine centre set up in a cluster of apartment blocks in an industrial part of Wuhan.</p>''')

    def test_articles_count(self):
        articles = Article.objects
        self.assertEqual(articles.count(), 4)

    def test_title_search_count(self):
        article = Article.objects.filter(title__icontains='the')
        article2 = Article.objects.filter(title__icontains=' a ')
        self.assertEqual(article.count(), 0)
        self.assertEqual(article2.count(), 3)

    def test_brief_search_count(self):
        article = Article.objects.filter(brief__icontains='in')
        article2 = Article.objects.filter(brief__icontains='pandemic')
        self.assertEqual(article.count(), 3)
        self.assertEqual(article2.count(), 1)

    def test_union_search_count(self):
        query1 = "coronavirus"
        query2 = "and"
        article = Article.objects.filter(Q(title__icontains=query1) |
                                         Q(free_text__icontains=query1) |
                                         Q(pay_text__icontains=query1))
        article2 = Article.objects.filter(Q(title__icontains=query2) |
                                          Q(free_text__icontains=query2) |
                                          Q(pay_text__icontains=query2))
        self.assertEqual(article.count(), 2)
        self.assertEqual(article2.count(), 4)
