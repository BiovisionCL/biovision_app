
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/main.dart';

void main() {
  testWidgets('Widget principal carga sin errores', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());
    expect(find.byType(MyApp), findsOneWidget);
  });
}
