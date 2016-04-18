require 'sinatra'
require 'haml'
require 'elasticsearch'

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

  haml :search
end
