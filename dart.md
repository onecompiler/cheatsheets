# dart:core

Built-in Types

Numbers: num, int, double
Strings: String, StringBuffer, RegExp
Booleans: bool, true, false
Dates & Times: DateTime, Duration, Stopwatch
Collections: List<E>, Set<E>, Map<K, V>
Object

int hashCode
Type runtimeType
String toString()
Annotations

@deprecated
@override
@proxy
RegExp

Iterable<Match> allMatches(String str)
Match firstMatch(String str)
bool hasMatch(String str)
  
  
  
# dart:async
  
Completer<T>

Future future
bool complete([T value])
completeError(exception)
Future<T>

new Future(computation())
new Future.delayed(duration, [compute()])
new Future.value(value)
new Future.error(error)
Future<List> Future.wait(futures)
Future Future.forEach(iterable, Future f(e))
Future Future.doWhile(f())
Stream<T> asStream()
Future catchError(onError(error))
Future then(onValue(value))
Future whenComplete(action())
Stream<T>

new Stream.fromIterable(iterable)
new Stream.fromFuture(future)
new Stream.periodic(period)
new Stream.empty()
Future<bool> get isEmpty
Future<int> get length
Future<T> get first
Future<T> get last
Future<T> get single
bool get isBroadcast
Future<bool> any(predicate)
Stream<T> asBroadcastStream()
Stream<T> distinct()
Stream<T> skip(count)
Stream<T> skipWhile(predicate)
Stream<T> take(count)
Stream<T> where(predicate)
Stream<T> takeWhile(predicate)
Stream expand(Iterable convert(T value))
Stream map(convert(T event))
Stream transform(streamTransformer)
Stream<T> handleError(handle(error))
StreamSubscription listen(onData(event))
Future pipe(streamConsumer)
Future<bool> contains(T match)
Future<T> elementAt(index)
Future<bool> every(predicate)
Future<T> firstWhere(predicate)
Future<T> lastWhere(predicate)
Future<T> singleWhere(predicate)
Future<T> reduce(combine(previous, e))
Future fold(initValue, combine(previous, e))
Future<List<T>> toList()
Future<Set<T>> toSet()
Timer

Timer.run(callback()))
new Timer(duration, callback())
new Timer.periodic(duration, callback())
cancel()
Zone

runZoned(() {
  new Future(() => throw "async error");
}, onError: (e) => print("Async error: $e"))
  
  
# Keywords
  
Library: library, part, part of, import, export, show, hide, deferred
Class: class, enum, abstract, extends, implements, this, super, with
Constructor: new, factory, const
Function: operator, external
Getter / Setter: get, set
Type: void, null, var, dynamic, typedef, is, as, false, true
Modifier: static, final, const
Control flow: if, else, for, in, while, do, break, continue, return, switch, case, default, assert
Asynchrony: await, async, async*, sync*, yield, yield*
Exception: try, catch, finally, throw, rethrow
  
  
# dart:io
  
File

Directory
File
Encoding
Stream

LineTransformer
StringDecoder
StringEncoder
System

Platform
Process
HTTP

ContentType
Cookie
HttpHeaders
HttpSession
HttpClient
HttpServer
WebSocket
Socket
  
  
# package:http

HTTP Client

Future<String> read(url)
Future<Response> get(url)
Future<Response> post(url)
Future<Response> put(url)
Future<Response> delete(url)
Future<Response> head(url)
Example

var resp = await http.get(url);
print("Response status: ${resp.statusCode}");
print("Response body: ${resp.body}");
  
  

# package:http_server

HTTP Server

VirtualDirectory
VirtualHost
HttpBody
HttpBodyFileUpload
HttpBodyHandler
HttpClientResponseBody
HttpMultipartFormData
HttpRequestBody
Example

var staticFiles = new VirtualDirectory('.')
  ..allowDirectoryListing = true;
var server = await HttpServer.bind('0.0.0.0', 7777);
print('Server running');
server.listen(staticFiles.serveRequest);
  
  
  
# dart:isolate
  
  
Classes

Isolate
Capability
ReceivePort
SendPort
Isolate

Isolate.spawn(entryPoint(msg), msg)
Isolate.spawnUri(Uri uri, List args, msg)
SendPort controlPort
Stream errors
pause()
resume()
kill()
Examples

Isolate.spawn(entryPoint, "Hello");
entryPoint(msg) 
  => print("$msg from isolate!");

Isolate.spawnUri(new Uri.file("hello.dart"),
  [], "World");
  
  
# dart:mirrors
  
 MirrorSystem currentMirrorSystem()
InstanceMirror reflect(Object reflectee)
ClassMirror reflectClass(Type key)
TypeMirror reflectType(Type key)
  
  
# dart:collection
  
  
 	Unordered	Ordered	Sorted
List		List	
Set	HashSet	LinkedHashSet	SplayTreeSet
Map	HashMap	LinkedHashMap	SplayTreeMap
Iterable

const Iterable.empty()
new Iterable.generate(count, generator(i))
bool isEmpty
bool isNotEmpty
Iterator<E> iterator
int length
E first
E single
E last
E elementAt(index)
E firstWhere(predicate)
E lastWhere(predicate)
singleWhere(predicate)
bool contains(e)
bool any(predicate)
bool every(predicate)
Iterable map(f(E e))
Iterable expand(Iterable f(E e))
Iterable<E> where(predicate)
forEach(f(E e))
Iterable<E> skip(n)
Iterable<E> skipWhile(predicate)
Iterable<E> take(n)
Iterable<E> takeWhile(predicate)
E reduce(combine(E value, E e))
fold(initValue, combine(previous, e))
String join([separator])
List<E> toList()
Set<E> toSet()
List

add(E e)
insert(index, E e)
addAll(Iterable<E> elements)
remove(Object element)
retainWhere(predicate)
insertAll(index, Iterable<E> iterable)
setAll(index, Iterable<E> iterable)
clear()
E operator [ ](index)
operator [ ]=(index, E value)
Iterable<E> get reversed
sort([comparator])
indexOf(E e, [start = 0])
int lastIndexOf(E e, [start])
E removeAt(index)
E removeLast()
List<E> sublist(int start, [int end])
removeRange(int start, int end)
fillRange(int start, int end, [E fillValue])
replaceRange(int start, int end, Iterable<E> iterable)
setRange(start, end, Iterable<E> iterable)
Map<int, E> asMap()
Map

clear()
bool containsValue(V value)
bool containsKey(K key)
V operator [ ](K key)
operator [ ]=(K key, V value)
V putIfAbsent(K key, V ifAbsent())
V remove(K key)
forEach(f(K key, V value))
Iterable<K> get keys
Iterable<V> get values
