from client import MultiModalChartGraphDataExtractorClient

def main():
    client = MultiModalChartGraphDataExtractorClient()
    res = client.extract_chart_data_table('https://example.com/bar_chart.png')
    print('Multi-Modal Chart Extractor: ' + res['chart_extraction_id'] + ' (Type: ' + res['detected_chart_type'] + ')')
    print('Confidence: ' + str(res['ocr_data_point_confidence_score']))
    print('Markdown Table:\n' + res['extracted_markdown_table'])
    print('Dataframe JSON: ' + res['structured_dataframe_json_url'])

if __name__ == '__main__':
    main()
