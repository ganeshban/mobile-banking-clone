import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiRequest {
  final String baseUrl;
  String port = '';
  Map<String, String> header = {
    'Content-Type': 'application/json; charset=UTF-8'
  };
  final List<String> _paths = [];
  final List<String> _query = [];

  ApiRequest(this.baseUrl, this.port);

  void addPaths(List<String> paths) {
    _paths.addAll(paths);
  }

  void replacePath(String newPath, {int index = 0}) {
    _paths[index] = newPath;
  }

  void removePath({int index = -1}) {
    int i = index;
    if (index == -1) {
      i = _paths.length;
    }
    _paths.removeAt(i);
  }

  void clearPath() {
    _paths.clear();
  }

  void addPath(String path) {
    _paths.add(path);
  }

  void addQuerys(List<String> querys) {
    _query.addAll(querys);
  }

  void addQuery(String query) {
    _query.add(query);
  }

  String getFullPath() {
    String url = baseUrl;
    if (port.isNotEmpty) {
      url = url + ':' + port;
    }
    if (_paths.isNotEmpty) {
      url = url + '/' + _paths.join('/');
    }
    if (_query.isNotEmpty) {
      url = url + '?' + _query.join('&');
    }
    return url;
  }

  String getPathOnly() {
    return _paths.join('/');
  }

  String getQueryOnly() {
    return _query.join('&');
  }

  Future<String> get() async {
    final response = await http.get(
      Uri.parse(getFullPath()),
      headers: header,
    );
    return response.body;
  }

  Future<String> post(String postBody) async {
    final response = await http.post(
      Uri.parse(getFullPath()),
      headers: header,
      body: postBody,
    );
    return response.body;
  }
}

void main(List<String> args) async {
  var api = ApiRequest('http://127.0.0.1', '8000');
  // http://127.0.0.1:8000/login?username=ganesh&password=ban123
  // api.addPath('path2');
  api.addPath('login');
  api.addQuerys(['username=ganesh', 'password=baanana']);
  var resp = await api.get();
  var jsonData = jsonDecode(resp);
  // print(jsonData);
  print(jsonData['detail']['data']);
  // print(resp.toString());
}
