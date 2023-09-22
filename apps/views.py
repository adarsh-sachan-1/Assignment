""""
apps views
"""
# local imports
from .scripts import scrape_and_save_article
from .serializers import ArticleSerializer
from .models import Article
# django imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ScrapeArticleView(APIView):
    """
    Scrapper this class to fetch data given url.
    """
    def post(self, request, format=None):
        """
        :param request:
        :param format:
        :return:
        """
        url_to_scrape = "https://pubmed.ncbi.nlm.nih.gov/36381921/"

        result = scrape_and_save_article(url_to_scrape)

        if result["status"] == "success":
            return Response({"message": "Article saved successfully."})
        else:
            return Response({"error": result["message"]}, status=500)


class ArticleListView(APIView):
    """
    get data all list
    """
    def get(self, request, format=None):
        """
        :param request:
        :param format: None
        :return: json data
        """
        # Retrieve a list of all articles
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    """
    get data detail pass pk = pmid show detail this id's data
    """
    def get(self, request, pk, format=None):
        """
        :param request:
        :param pk: str
        :param format: None
        :return: json data
        """
        try:
            # Retrieve a specific article by primary key (pmid)
            article = Article.objects.get(pmid=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({"error": "Article not found."}, status=status.HTTP_404_NOT_FOUND)