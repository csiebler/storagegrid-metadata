require 'sinatra'
require 'haml'
require 'elasticsearch'

sgurl = "https://10.10.4.110:8082/"
config = {
  host: "elasticsearch:9200"
}
client = Elasticsearch::Client.new(config)

get "/" do
  haml :index
end

get "/search" do
  @query = params['query']

  response = client.search index: 'objects', q: @query
  @num_results = response['hits']['total']
  @results = response['hits']['hits']
  @time = response['took']
  @endpoint = sgurl

  haml :search
end
