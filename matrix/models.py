from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import uuid


class Survey(models.Model):
    q01_products = models.CharField(max_length=256, default="", blank=True)
    q02_project_name = models.CharField(max_length=256, default="", blank=True)
    q04_doi = models.CharField(max_length=256, default="", blank=True)
    q04_doi_other = models.CharField(max_length=256, default="", blank=True)
    q05_products_posted = models.CharField(max_length=256, default="", blank=True)
    q05_products_posted_other = models.CharField(max_length=256, default="", blank=True)
    q05_products_repo_other = models.CharField(max_length=256, default="", blank=True)
    q06_simulations = models.CharField(max_length=256, default="", blank=True)
    q07_license = models.CharField(max_length=256, default="", blank=True)
    q08_license_other = models.CharField(max_length=256, default="", blank=True)
    q08_license_other_institutional = models.CharField(
        max_length=256, default="", blank=True
    )
    q08_license_other_none = models.CharField(max_length=256, default="", blank=True)
    q09_open_data = models.CharField(max_length=256, default="", blank=True)
    q10_indigenous_populations = models.CharField(
        max_length=256, default="", blank=True
    )
    q11_specialized_software_open_source = models.CharField(
        max_length=256, default="", blank=True
    )
    q12_specialized_software = models.CharField(max_length=256, default="", blank=True)
    q12_specialized_software_specify = models.CharField(
        max_length=256, default="", blank=True
    )
    q13_existing_libraries = models.CharField(max_length=256, default="", blank=True)
    q14_nano_publications = models.CharField(max_length=256, default="", blank=True)
    q14_nano_other = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_csv = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_database = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_hd5f = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_json = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_other = models.CharField(max_length=256, default="", blank=True)
    q15_data_formats_other_value = models.CharField(
        max_length=256, default="", blank=True
    )
    q15_data_formats_spreadsheet = models.CharField(
        max_length=256, default="", blank=True
    )
    q16_notebooks_shared = models.CharField(max_length=256, default="", blank=True)
    q16_notebooks_other = models.CharField(max_length=256, default="", blank=True)
    q17_notebooks_template = models.CharField(max_length=256, default="", blank=True)
    q17_notebooks_template_other = models.CharField(
        max_length=256, default="", blank=True
    )
    q18_software_license = models.CharField(max_length=256, default="", blank=True)
    q18_software_license_other = models.CharField(
        max_length=256, default="", blank=True
    )
    q19_api = models.CharField(max_length=256, default="", blank=True)
    q33_smart_api = models.CharField(max_length=256, default="", blank=True)
    q20_api_versioned = models.CharField(max_length=256, default="", blank=True)
    q22_ML_code = models.CharField(max_length=256, default="", blank=True)
    q22_ML_code_other = models.CharField(max_length=256, default="", blank=True)
    q26_ML_models_shared = models.CharField(max_length=256, default="", blank=True)
    q26_ML_models_other = models.CharField(max_length=256, default="", blank=True)
    q25_ML_repro = models.CharField(max_length=256, default="", blank=True)
    q25_ML_repro_consider_other = models.CharField(
        max_length=256, default="", blank=True
    )
    q27_domain_repo_other = models.CharField(max_length=256, default="", blank=True)
    q28_dmp = models.CharField(max_length=256, default="", blank=True)
    q29_register_repo = models.CharField(max_length=256, default="", blank=True)
    q29_register_repo_other = models.CharField(max_length=256, default="", blank=True)
    q30_schema_org = models.CharField(max_length=256, default="", blank=True)
    q64_email_address = models.CharField(max_length=256, default="", blank=True)
    random_id = models.CharField(max_length=256, default="", blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def q01_products_list(self):
        return [x.strip() for x in self.q01_products.split(",")]

    def q05_products_posted_list(self):
        products_posted = [x.strip() for x in self.q05_products_posted.split(",")]

        if "Other (Specify)".casefold() in map(str.casefold, products_posted):
            products_posted.remove("Other (Specify)")
            products_posted.append(self.q05_products_posted_other)

        return products_posted

    def q15_data_formats_csv_list(self):
        return [x.strip() for x in self.q15_data_formats_csv.split(",")]

    def q15_data_formats_database_list(self):
        return [x.strip() for x in self.q15_data_formats_database.split(",")]

    def q15_data_formats_hd5f_list(self):
        return [x.strip() for x in self.q15_data_formats_hd5f.split(",")]

    def q15_data_formats_json_list(self):
        return [x.strip() for x in self.q15_data_formats_json.split(",")]

    def q15_data_formats_other_list(self):
        return [x.strip() for x in self.q15_data_formats_other.split(",")]

    def q15_data_formats_spreadsheet_list(self):
        return [x.strip() for x in self.q15_data_formats_spreadsheet.split(",")]

    def q15_input_data_list(self):
        input = []

        if "input".casefold() in map(str.casefold, self.q15_data_formats_csv_list()):
            input.append("CSV")
        if "input".casefold() in map(
            str.casefold, self.q15_data_formats_database_list()
        ):
            input.append("Database")
        if "input".casefold() in map(str.casefold, self.q15_data_formats_hd5f_list()):
            input.append("HDF5")
        if "input".casefold() in map(str.casefold, self.q15_data_formats_json_list()):
            input.append("JSON")
        if "input".casefold() in map(
            str.casefold, self.q15_data_formats_spreadsheet_list()
        ):
            input.append("Spreadsheet")
        if "input".casefold() in map(str.casefold, self.q15_data_formats_other_list()):
            input.append(self.q15_data_formats_other_value)

        return input

    def q15_output_data_list(self):
        output = []

        if "output".casefold() in map(str.casefold, self.q15_data_formats_csv_list()):
            output.append("CSV")
        if "output".casefold() in map(
            str.casefold, self.q15_data_formats_database_list()
        ):
            output.append("Database")
        if "output".casefold() in map(str.casefold, self.q15_data_formats_hd5f_list()):
            output.append("HDF5")
        if "output".casefold() in map(str.casefold, self.q15_data_formats_json_list()):
            output.append("JSON")
        if "output".casefold() in map(
            str.casefold, self.q15_data_formats_spreadsheet_list()
        ):
            output.append("Spreadsheet")
        if "input".casefold() in map(str.casefold, self.q15_data_formats_other_list()):
            output.append(self.q15_data_formats_other_value)

        return output

    def save(self, *args, **kwargs):
        # Generate a random id for the survey
        self.random_id = uuid.uuid4()

        # Save the results of the survey to the database
        super(Survey, self).save(*args, **kwargs)

        # Get the primary key of the survey and create the survey url
        survey_url = "http://%s/matrix/%s/" % (
            settings.DOMAIN_NAME,
            str(self.random_id),
        )

        print("New survey sent: %s" % survey_url)

        send_mail(
            "Link to Fair Data Survey",
            "Survey URL: %s" % survey_url,
            settings.DEFAULT_FROM_EMAIL,
            [self.q64_email_address],
            fail_silently=settings.EMAIL_FAIL_SILENTLY,
        )
