
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/features/home/presentation/home_page.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('Counter increments smoke test en HomePage', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: HomePage()));

    // Verifica que el contador inicia en 0.
    expect(find.text('0'), findsOneWidget);
    expect(find.text('1'), findsNothing);

    // Simula un tap en el botón "Presióname".
    await tester.tap(find.text('Presióname'));
    await tester.pump();

    // Verifica que el contador incrementó a 1.
    expect(find.text('0'), findsNothing);
    expect(find.text('1'), findsOneWidget);
  });
}
