class MultiModalChartGraphDataExtractorClient:
    def extract_chart_data_table(self, chart_image_url='https://storage.genpark.ai/charts/sales_growth_2026.png', chart_type_hint='LINE_CHART_DUAL_AXIS'):
        return {
            'chart_extraction_id': 'chr_ext_7721',
            'detected_chart_type': 'DUAL_AXIS_BAR_LINE_CHART',
            'extracted_markdown_table': '| Quarter | Revenue ($M) | Gross Margin (%) |\n|---|---|---|\n| Q1 2026 | 120.5 | 68.2% |\n| Q2 2026 | 148.0 | 71.4% |\n| Q3 2026 | 185.2 | 74.0% |',
            'ocr_data_point_confidence_score': 0.989,
            'structured_dataframe_json_url': 'https://charts.vision.genpark.ai/data/7721.json'
        }
