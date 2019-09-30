from django.test import TestCase, Client
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from .models import Catalogue
from .forms import CatalogueForm, BidForm

class TestDisplayViews(TestCase):

    def test_display_all_view(self):
        page = self.client.get("/auctions/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "display-all.html")


    def test_display_era_view(self):
        page = self.client.get("/auctions/era1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "display-era.html")
